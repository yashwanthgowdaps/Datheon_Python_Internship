# Task 1: Hangman
# Datheon Python Programming Internship

import random

MAX_ATTEMPTS = 6

# Index = number of wrong guesses (0 to 6). Raw strings keep backslashes intact.
STAGES = [
    r"""
     +---+
     |   |
         |
         |
         |
    =======
    """,
    r"""
     +---+
     |   |
     O   |
         |
         |
    =======
    """,
    r"""
     +---+
     |   |
     O   |
     |   |
         |
    =======
    """,
    r"""
     +---+
     |   |
     O   |
    /|   |
         |
    =======
    """,
    r"""
     +---+
     |   |
     O   |
    /|\  |
         |
    =======
    """,
    r"""
     +---+
     |   |
     O   |
    /|\  |
    /    |
    =======
    """,
    r"""
     +---+
     |   |
     O   |
    /|\  |
    / \  |
    =======
    """,
]

WORDS = ["python", "computer", "program", "developer", "keyboard"]


def draw_hangman(attempts_left):
    """Draw the hangman for the number of attempts still remaining."""
    print(STAGES[MAX_ATTEMPTS - attempts_left])


def build_display(secret_word, guessed_letters):
    """Return the word with unguessed letters hidden."""
    return " ".join(
        letter if letter in guessed_letters else "_" for letter in secret_word
    )


def has_won(secret_word, guessed_letters):
    return all(letter in guessed_letters for letter in secret_word)


def play():
    secret_word = random.choice(WORDS)
    guessed_letters = []
    attempts = MAX_ATTEMPTS

    print("===== WELCOME TO HANGMAN =====")

    while attempts > 0 and not has_won(secret_word, guessed_letters):
        draw_hangman(attempts)
        print("Word:", build_display(secret_word, guessed_letters))
        print("Attempts remaining:", attempts)
        if guessed_letters:
            print("Guessed letters:", ", ".join(sorted(guessed_letters)))

        guess = input("Guess a single letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter only one letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print("Correct guess!")
        else:
            attempts -= 1
            print("Wrong guess!")

    if has_won(secret_word, guessed_letters):
        print("\nWord:", build_display(secret_word, guessed_letters))
        print("Congratulations! You guessed the word:", secret_word)
    else:
        draw_hangman(0)
        print("Game over!")
        print("The correct word was:", secret_word)

    print("Thanks for playing!")


def main():
    try:
        play()
    except (EOFError, KeyboardInterrupt):
        print("\nGame cancelled. Goodbye!")


if __name__ == "__main__":
    main()
