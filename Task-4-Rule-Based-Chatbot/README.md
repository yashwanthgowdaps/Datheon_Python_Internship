# Task 4: Rule-Based Interactive Terminal Assistant / Chatbot

**PyBot** is a customer-support chatbot for a sample shop called *TechNest*. It recognises what the user is asking using regular expressions and answers from a JSON FAQ file.

## Features

- **Multi-intent recognition** with regular expressions (hours, products, prices, shipping, returns, warranty, payments, order tracking, contact)
- **FAQ data in JSON** (`faq.json`): change the business details without touching the code
- **Business hours**: answers "when are you open?" and "are you open now?" using the real clock
- **Conversation flow**: greeting, intent identification, resolution, then "Anything else?" and exit
- "Tell me more" follow-ups for the previous topic
- **Fallback handling** for unrecognised questions, with extra help after repeated misses
- Clean exit commands: `bye`, `exit`, `quit`
- Handles empty input, missing or broken `faq.json`, and Ctrl+C

## How to Run

```
python Task-4-Rule-Based-Chatbot/chatbot.py
```

`faq.json` must stay in the same folder as `chatbot.py` (the bot falls back to a small built-in FAQ if it is missing).

## Example

```
You: hello
PyBot: Hello! Welcome to TechNest support. How can I help you?

You: what are your business hours
PyBot: Our business hours are: Monday to Friday: 9:00 AM - 6:00 PM, ... Is there anything else I can help you with?

You: how much is a laptop?
PyBot: Accessories start at Rs. 299, headphones at Rs. 1,499, ... Is there anything else I can help you with?

You: no
PyBot: Goodbye! Thank you for contacting TechNest. Have a great day.
```

## Adding Your Own Questions

Add an entry to the `intents` list in `faq.json`:

```json
{
  "name": "location",
  "patterns": ["\\b(where|address|location)\\b"],
  "responses": ["We are located at 12 Main Road, Bengaluru."]
}
```

## Limitations

PyBot uses fixed rules rather than machine learning, so it only understands the topics in `faq.json`. Unusual phrasings may fall back to the default reply.

## Python Concepts Used

Regular expressions (`re`), JSON (`json`), classes and state tracking, dictionaries and lists, `datetime`, loops, exception handling.
