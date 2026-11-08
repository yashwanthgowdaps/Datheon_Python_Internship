# Task 4: Basic Rule-Based Chatbot
# Datheon Python Programming Internship

import random
import re
from datetime import datetime

EXIT_WORDS = {"bye", "goodbye", "exit", "quit"}
GREETINGS = {"hi", "hello", "hey", "good morning",
             "good afternoon", "good evening"}


def normalize(text):
    """Lowercase, unify apostrophes, drop punctuation, collapse spaces."""
    text = text.lower().replace("\u2019", "'")
    text = re.sub(r"[^a-z0-9' ]+", " ", text)
    return " ".join(text.split())


def is_exit(user_input):
    return normalize(user_input) in EXIT_WORDS


def chatbot_response(user_input):
    """Generate responses using predefined rules."""
    message = normalize(user_input)
    words = set(message.split())

    if message in EXIT_WORDS or (words & EXIT_WORDS and len(words) <= 4):
        return "Goodbye! Have a great day."

    if message in GREETINGS:
        return random.choice([
            "Hello! How can I help you?",
            "Hi there! Nice to meet you.",
            "Hey! What can I do for you?",
        ])

    if "how are you" in message:
        return "I am doing well! Thank you for asking."

    if "your name" in message or message in {"name", "who are you"}:
        return "My name is PyBot. I am a rule-based chatbot."

    if "time" in words and ("what" in words or "what's" in words
                            or "tell" in words or message == "time"):
        return "Current time: " + datetime.now().strftime("%I:%M %p")

    if "date" in words or "today's date" in message:
        return "Today's date: " + datetime.now().strftime("%d-%m-%Y")

    if message == "help":
        return (
            "Here are some things you can ask me:\n"
            "- Say hello or hi\n"
            "- Ask my name\n"
            "- Ask how I am\n"
            "- Ask for the time\n"
            "- Ask for today's date\n"
            "- Ask my favourite colour\n"
            "- Ask what I can do\n"
            "- Say thank you\n"
            "- Type bye to exit"
        )

    if words & {"thank", "thanks"} or "thank you" in message:
        return "You're welcome! Happy to help."

    if "favourite colour" in message or "favorite color" in message:
        return "I like blue! What is your favourite colour?"

    if "i am fine" in message or "i'm fine" in message \
            or "i am good" in message or "i'm good" in message:
        return "That's great to hear!"

    if "what can you do" in message:
        return ("I can respond to greetings, tell the date and time, "
                "and answer simple questions.")

    return "Sorry, I don't understand that. Type 'help' to see what I can do."


def main():
    """Run the chatbot."""
    print("=" * 40)
    print("       WELCOME TO PYBOT")
    print("=" * 40)
    print("I am a simple rule-based chatbot.")
    print("Type 'help' to see available commands.")
    print("Type 'bye' to end the conversation.")

    while True:
        try:
            user_input = input("\nYou: ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break

        if not user_input:
            print("PyBot: Please enter a message.")
            continue

        response = chatbot_response(user_input)
        print("PyBot:", response)

        if response == "Goodbye! Have a great day.":
            break

    print("\nChatbot session ended. Thank you!")


if __name__ == "__main__":
    main()
