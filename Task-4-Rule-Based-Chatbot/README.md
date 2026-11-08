Task 4: Basic Rule-Based Chatbot

Internship: Datheon Python Programming Internship
Project Name: PyBot
Programming Language: Python 3

1. About the Project

PyBot is a basic rule-based chatbot developed using Python. It interacts with users through text messages and responds according to predefined rules and keywords.

The chatbot can respond to greetings, answer simple questions, display the current date and time, provide help, and end a conversation.

This project demonstrates fundamental Python programming concepts and basic conversational logic.

2. Features

- Greeting responses: Responds to greetings such as hello, hi, and hey.
- Name identification: Tells the user the chatbot's name.
- Simple conversation: Responds to messages such as "i am fine", "what can you do" and "what is your favourite colour" ("favorite color" also works).
- Date and time: Displays the current date and time.
- Help command: Lists the supported commands.
- Thank-you responses: Responds to thank-you messages.
- Flexible matching: Ignores capital letters and punctuation, so "Hello!" and "What's the time?" work.
- Input validation: Handles empty messages.
- Unknown input handling: Provides a default response when a message is not recognized.
- Exit option: Ends the conversation when the user says bye, goodbye, exit, or quit (for example "ok bye"), and also on Ctrl+C or Ctrl+D.
- Continuous interaction: Keeps running until the user exits.

3. Technologies Used

- Python 3
- "random" module
- "datetime" module
- "re" module

4. Python Concepts Used

- Variables and strings
- Functions
- Conditional statements ("if", "elif", "else")
- "while" loop
- Lists and sets
- String methods such as "lower()" and "strip()"
- Regular expressions ("re" module) to clean up the input
- User input and output
- Modules and imports
- Basic input validation

5. Project Structure

Task-4-Rule-Based-Chatbot/
├── chatbot.py
└── README.md

6. How to Run the Project

Using Pydroid 3 on Android

1. Install and open Pydroid 3.
2. Create a Python file named "chatbot.py".
3. Paste the chatbot source code into the file.
4. Save the file.
5. Press the Run button.
6. Enter a message in the console to interact with PyBot.

Using a Computer

1. Install Python 3.
2. Open a terminal in the project folder.
3. Run the following command:

python chatbot.py

If your system uses "python3", run:

python3 chatbot.py

No additional third-party packages are required.

7. Example Interaction

WELCOME TO PYBOT

You: hello
PyBot: Hi there! Nice to meet you.

You: what is your name
PyBot: My name is PyBot. I am a rule-based chatbot.

You: help
PyBot: Here are some things you can ask me...

You: bye
PyBot: Goodbye! Have a great day.

Chatbot session ended. Thank you!

8. Limitations

- PyBot uses predefined rules rather than artificial intelligence or machine learning.
- It recognizes only the messages covered by its programmed conditions.
- Matching is keyword-based, so unusual phrasings may not be understood.
- It cannot understand complex questions or generate unrestricted responses.
- Its responses may vary for greetings because it selects from predefined alternatives.

9. Learning Outcomes

Through this project, I practised writing Python functions, using conditional statements and loops, processing user input, importing standard library modules, and building a simple interactive application.

10. AI Assistance

AI assistance was used as a learning aid during development. The source code was reviewed and tested during development to understand the program's functionality.

11. Conclusion

PyBot demonstrates how a simple text-based chatbot can be created using core Python programming concepts. It provides a foundation for learning more advanced chatbot development and conversational systems.

Project: Datheon Python Programming Internship — Task 4: Basic Rule-Based Chatbot
