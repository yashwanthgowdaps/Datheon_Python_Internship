# Task 1: Hangman Word Guessing Game (Console)

A terminal Hangman game. The player guesses a hidden word one letter at a time and has **6 attempts**.

## Features

- Random word selection (`random.choice`)
- Masked word display, for example `P Y _ H O N`
- ASCII gallows art that updates with every wrong guess
- Tracks previously guessed letters
- Repeated guesses are detected and **not penalised**
- Input validation (a single letter only)
- Clear victory and game-over screens
- Play-again option, and a clean exit on Ctrl+C
- Optional word list: put a `words.txt` file (one word per line) next to `hangman.py` and the game uses it instead of the built-in list

## How to Run

```
python Task-1-Hangman/hangman.py
```

## Example

```
     +---+
     |   |
     O   |
    /|   |
         |
    =======

Word: P Y _ _ _ _
Attempts remaining: 3
Guessed letters: a, p, y, z
Guess a single letter:
```

## Python Concepts Used

Lists and strings, loops and conditionals, functions and constants, raw strings, file reading with error handling, input validation.
