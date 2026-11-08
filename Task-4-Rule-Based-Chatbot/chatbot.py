# Task 4: Rule-Based Chatbot
# Datheon Python Programming Internship

import random
from datetime import datetime

def chatbot_response(user_input):
    """Generate a response based on the user's message."""

    message = user_input.lower().strip()

    # Greeting
    if message in ["hello", "hi", "hey", "good morning", "good evening"]:
        return random.choice([
            "Hello! How can I help you?",
            "Hi there! Nice to meet you.",
            "Hey! What can I do for you?"
        ])

    # Ask the chatbot's name
    elif "your name" in message or message == "name":
        return "I am PyBot, a simple rule-based chatbot."

    # Ask how the chatbot is
    elif "how are you" in message:
        return "I am doing well! Thank you for asking."

    # Ask the time
    elif "time" in message:
        return "The current time is " + datetime.now().strftime("%I:%M %p")

    # Ask the date
    elif "date" in message:
        return "Today's date is " + datetime.now().strftime("%d-%m-%Y")

    # Ask for help
    elif "help" in message:
        return (
            "You can say hello, ask my name, ask how I am, "
            "ask for the time or date, or say goodbye."
        )

    # Thank you
    elif "thank" in message:
        return "You're welcome! Happy to help."

    # Goodbye
    elif any(word in message for word in ["bye", "goodbye", "exit", "quit"]):
        return "Goodbye! Have a great day."

    # Default response
    else:
        return "Sorry, I don't understand that yet. Type 'help' to see what I can do."


def main():
    """Start the chatbot conversation."""

    print("=" * 40)
    print("       WELCOME TO PYBOT")
    print("=" * 40)
    print("I am a simple rule-based chatbot.")
    print("Type 'help' for available commands.")
    print("Type 'bye' to end the conversation.")

    while True:
        user_input = input("\nYou: ").strip()

        if not user_input:
            print("PyBot: Please enter a message.")
            continue

        response = chatbot_response(user_input)
        print("PyBot:", response)

        message = user_input.lower().strip()

        if message in ["bye", "goodbye", "exit", "quit"]:
            break

    print("\nChatbot session ended. Thank you!")


if __name__ == "__main__":
    main()