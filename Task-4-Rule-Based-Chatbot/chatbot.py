# Task 4: Rule-Based Interactive Terminal Assistant / Chatbot
# Datheon Python Programming Internship
#
# A customer-support bot for a sample shop ("TechNest").
# Intents (regex patterns + responses) are loaded from faq.json, so the
# business details can be changed without touching this code.

import json
import os
import random
import re
from datetime import datetime

FAQ_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "faq.json")

EXIT_PATTERN = re.compile(r"\b(bye|goodbye|exit|quit)\b")
NO_PATTERN = re.compile(
    r"^(no|nope|nah|nothing|no thanks|no thank you|that'?s all|that is all|"
    r"i'?m good|im good|all good)$"
)
YES_PATTERN = re.compile(r"^(yes|yeah|yep|yup|sure|ok|okay|please)$")
MORE_PATTERN = re.compile(r"\b(more|details|explain|elaborate|tell me more)\b")

FOLLOW_UP = "Is there anything else I can help you with?"
GOODBYE = "Goodbye! Thank you for contacting TechNest. Have a great day."
FALLBACKS = [
    "Sorry, I didn't understand that. Try asking about hours, products, "
    "prices, shipping, returns or warranty.",
    "I'm not sure about that one. Type 'help' to see what I can answer.",
]

# Used only if faq.json is missing or broken.
DEFAULT_FAQ = {
    "business": {"name": "TechNest", "bot_name": "PyBot"},
    "hours": {str(d): [9, 18] for d in range(6)} | {"6": None},
    "hours_text": "Monday to Saturday: 9:00 AM - 6:00 PM, Sunday: closed.",
    "intents": [
        {
            "name": "greeting",
            "patterns": [r"\b(hi|hello|hey)\b"],
            "responses": ["Hello! How can I help you?"],
            "followup": False,
        },
        {
            "name": "hours",
            "patterns": [r"\bhours\b", r"\bwhen .*open\b"],
            "responses": ["Our business hours are: {hours_text}"],
        },
    ],
}


def load_faq(path=FAQ_FILE):
    """Load and validate the FAQ data from JSON; fall back to a default."""
    try:
        with open(path, encoding="utf-8") as file:
            data = json.load(file)
        if not isinstance(data.get("intents"), list):
            raise ValueError("'intents' must be a list")
    except (OSError, ValueError) as error:
        print(f"[Warning] Could not load {os.path.basename(path)} ({error}). "
              "Using built-in defaults.")
        data = DEFAULT_FAQ

    # Compile the regular expressions once.
    for intent in data["intents"]:
        compiled = []
        for pattern in intent.get("patterns", []):
            try:
                compiled.append(re.compile(pattern, re.IGNORECASE))
            except re.error:
                print(f"[Warning] Bad pattern ignored in '{intent.get('name')}'.")
        intent["_compiled"] = compiled
    return data


def normalize(text):
    """Lowercase, unify apostrophes and collapse extra spaces."""
    text = text.lower().replace("\u2019", "'")
    return " ".join(text.split())


def match_intent(message, intents):
    """Return the best matching intent, or None if confidence is too low.

    The score is the length of the longest text matched by any of the
    intent's patterns, so more specific matches win over short ones.
    """
    best, best_score = None, 0
    for intent in intents:
        for pattern in intent["_compiled"]:
            found = pattern.search(message)
            if found and len(found.group(0)) > best_score:
                best, best_score = intent, len(found.group(0))
    return best


def open_status(faq, now=None):
    """Say whether the shop is open right now, using the hours in faq.json."""
    now = now or datetime.now()
    today = faq["hours"].get(str(now.weekday()))
    if today and today[0] <= now.hour + now.minute / 60 < today[1]:
        return (f"Yes, we are open right now (today until "
                f"{today[1] % 12 or 12}:00 {'AM' if today[1] < 12 else 'PM'}).")
    return f"Sorry, we are closed right now. Our hours: {faq['hours_text']}"


class ChatBot:
    """Conversation flow: greeting -> intent identification -> resolution -> exit."""

    def __init__(self, faq):
        self.faq = faq
        self.state = "idle"          # "idle" or "awaiting_more"
        self.last_intent = None
        self.misses = 0

    def respond(self, user_input):
        """Return (reply, finished)."""
        message = normalize(user_input)

        if not message:
            return "Please type a message.", False

        # 1. Exit commands (short messages only, so questions are not cut off).
        if len(message.split()) <= 4 and EXIT_PATTERN.search(message):
            return GOODBYE, True

        # 2. Answer to "Is there anything else?"
        if self.state == "awaiting_more":
            if NO_PATTERN.match(message):
                return GOODBYE, True
            if YES_PATTERN.match(message):
                self.state = "idle"
                return "Sure! What would you like to know?", False

        # 3. "Tell me more" about the previous topic.
        if self.last_intent and self.last_intent.get("details") \
                and MORE_PATTERN.search(message) and len(message.split()) <= 4:
            self.state = "awaiting_more"
            return self.last_intent["details"] + " " + FOLLOW_UP, False

        # 4. Intent identification.
        intent = match_intent(message, self.faq["intents"])
        if intent is None:
            self.misses += 1
            self.state = "idle"
            if self.misses >= 3:
                self.misses = 0
                return ("I'm having trouble understanding. Type 'help' for "
                        "topics or ask for 'contact' to reach our team."), False
            return random.choice(FALLBACKS), False

        # 5. Resolution.
        self.misses = 0
        self.last_intent = intent
        if intent.get("action") == "open_now":
            reply = open_status(self.faq)
        else:
            reply = random.choice(intent["responses"]).format(
                hours_text=self.faq["hours_text"]
            )

        if intent.get("followup", True):
            self.state = "awaiting_more"
            reply += " " + FOLLOW_UP
        else:
            self.state = "idle"
        return reply, False


def main():
    faq = load_faq()
    bot = ChatBot(faq)
    name = faq.get("business", {}).get("bot_name", "PyBot")

    print("=" * 44)
    print(f"  {faq.get('business', {}).get('name', 'Shop')} SUPPORT - {name}")
    print("=" * 44)
    print("Ask about hours, products, prices, shipping, returns or warranty.")
    print("Type 'help' for topics or 'bye' to exit.")

    while True:
        try:
            user_input = input("\nYou: ")
        except (EOFError, KeyboardInterrupt):
            print()
            break

        reply, finished = bot.respond(user_input)
        print(f"{name}: {reply}")
        if finished:
            break

    print("\nChat session ended.")


if __name__ == "__main__":
    main()
