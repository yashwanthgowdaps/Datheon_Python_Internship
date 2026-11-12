# Task 1: Hangman Word Guessing Game (Console)
# Datheon Python Programming Internship

import os
import random

MAX_ATTEMPTS = 6

# Index = number of wrong guesses (0 to 6). Raw strings keep the backslashes.
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

DEFAULT_WORDS = [
    "python", "computer", "program", "developer", "keyboard", "function",
    "variable", "internet", "software", "database", "network", "algorithm",
    "terminal", "compiler", "debugging", "library", "module", "string",
    "integer", "boolean", "console", "internship", "project", "internet",
]


def load_words():
    """Load words from words.txt (next to this script) if it exists.

    The file should have one word per line. Falls back to the built-in list.
    """
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "words.txt")
    words = []
    try:
        with open(path, encoding="utf-8") as file:
            for line in file:
                word = line.strip().lower()
                if word.isalpha() and len(word) >= 4:
                    words.append(word)
    except OSError:
        pass
    return words or DEFAULT_WORDS


def draw_hangman(attempts_left):
    """Draw the hangman for the number of attempts still remaining."""
    print(STAGES[MAX_ATTEMPTS - attempts_left])


def build_display(secret_word, guessed_letters):
    """Return the word with unguessed letters hidden, e.g. '_ A _ H E O N'."""
    return " ".join(
        letter.upper() if letter in guessed_letters else "_"
        for letter in secret_word
    )


def has_won(secret_word, guessed_letters):
    return all(letter in guessed_letters for letter in secret_word)


def play_round(words):
    secret_word = random.choice(words)
    guessed_letters = []
    attempts = MAX_ATTEMPTS

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
            # Repeated guesses are not penalised.
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
        print("VICTORY! You guessed the word:", secret_word)
    else:
        draw_hangman(0)
        print("GAME OVER! The correct word was:", secret_word)


def main():
    print("===== WELCOME TO HANGMAN =====")
    words = load_words()
    try:
        while True:
            play_round(words)
            again = input("\nPlay again? (y/n): ").strip().lower()
            if again not in ("y", "yes"):
                break
    except (EOFError, KeyboardInterrupt):
        print()
    print("Thanks for playing!")


if __name__ == "__main__":
    main()
