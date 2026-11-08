
import random

# Function to draw the hangman
def draw_hangman(attempts):
    stages = [
        """
         +---+
         |   |
         O   |
        /|\\  |
        / \\  |
        =======
        """,
        """
         +---+
         |   |
         O   |
        /|\\  |
        /    |
        =======
        """,
        """
         +---+
         |   |
         O   |
        /|\\  |
             |
        =======
        """,
        """
         +---+
         |   |
         O   |
        /|   |
             |
        =======
        """,
        """
         +---+
         |   |
         O   |
        /    |
             |
        =======
        """,
        """
         +---+
         |   |
         O   |
             |
             |
        =======
        """,
        """
         +---+
         |   |
             |
             |
             |
        =======
        """
    ]

    print(stages[attempts])


# List of words
words = ["python", "computer", "program", "developer", "keyboard"]

# Select a random word
secret_word = random.choice(words)

# Game variables
guessed_letters = []
attempts = 6

print("===== WELCOME TO HANGMAN =====")

# Main game loop
while attempts > 0:

    # Draw the hangman
    draw_hangman(attempts)

    # Display the word
    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("Word:", display_word)
    print("Attempts remaining:", attempts)

    # Check whether the player has won
    if all(letter in guessed_letters for letter in secret_word):
        print("Congratulations! You won!")
        break

    # Get the player's guess
    guess = input("Guess a single letter: ").lower().strip()

    # Validate the input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    # Check for repeated guesses
    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    # Store the guessed letter
    guessed_letters.append(guess)

    # Check the guess
    if guess in secret_word:
        print("Correct guess!")
    else:
        attempts -= 1
        print("Wrong guess!")


# Display the final result
if all(letter in guessed_letters for letter in secret_word):
    print("\nCongratulations! You guessed the word:", secret_word)
else:
    # Draw the complete hangman when the player loses
    draw_hangman(0)
    print("\nGame over!")
    print("The correct word was:", secret_word)

print("Thanks for playing!")
