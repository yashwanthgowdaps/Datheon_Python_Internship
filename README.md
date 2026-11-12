# Datheon Python Programming Internship

Four beginner-to-intermediate Python console projects built for the Datheon Python Programming Internship.

## Projects

| Task | Project | Script |
|------|---------|--------|
| 1 | Hangman Word Guessing Game | `Task-1-Hangman/hangman.py` |
| 2 | Stock Portfolio Performance Tracker | `Task-2-Stock-Portfolio/portfolio.py` |
| 3 | Automated File Organizer & Cleanup Utility | `Task-3-File-Automation/organizer.py` |
| 4 | Rule-Based Interactive Terminal Assistant / Chatbot | `Task-4-Rule-Based-Chatbot/chatbot.py` |

Each task folder has its own README with features, usage and examples.

## Repository Structure

```
Datheon_Python_Internship/
├── README.md
├── Task-1-Hangman/
│   ├── hangman.py
│   └── README.md
├── Task-2-Stock-Portfolio/
│   ├── portfolio.py
│   └── README.md
├── Task-3-File-Automation/
│   ├── organizer.py
│   └── README.md
└── Task-4-Rule-Based-Chatbot/
    ├── chatbot.py
    ├── faq.json
    └── README.md
```

## How to Run

Requires Python 3.8 or newer. No third-party packages are needed. From the repository root:

```
python Task-1-Hangman/hangman.py
python Task-2-Stock-Portfolio/portfolio.py
python Task-3-File-Automation/organizer.py
python Task-4-Rule-Based-Chatbot/chatbot.py
```

On some systems use `python3` instead of `python`. The projects also run in Pydroid 3 on Android.

## Technologies

Python 3 standard library only: `random`, `os`, `csv`, `json`, `re`, `shutil`, `pathlib`, `logging`, `datetime`.

## Notes

- Stock prices are sample data, not live market prices.
- Test the file organizer on a small sample folder first. It moves files.
- AI tools were used as a learning aid during development. I tested every program and reviewed the code to understand how it works.
