Task 2: Stock Portfolio Tracker

About

The Stock Portfolio Tracker is a Python-based console application developed as part of the Datheon Python Programming Internship.

It allows users to add stocks to a portfolio, view their holdings, calculate the total portfolio value, and save portfolio details to a text file.

Features

- Displays available stocks and their sample prices.
- Allows users to add stocks by entering a stock ticker and quantity.
- Supports multiple stock holdings.
- Calculates the value of each stock holding.
- Displays the total portfolio value.
- Validates stock tickers and share quantities.
- Saves portfolio details to "portfolio.txt" (UTF-8, so the rupee symbol is safe on any system).
- Uses one shared function to build the report, so the screen and the saved file always match.
- Provides a menu-driven interface to view, save, and exit.

Available Stocks

The program uses sample prices in Indian rupees (₹).

Stock Ticker| Sample Price
AAPL| ₹180.00
TSLA| ₹250.00
GOOGL| ₹150.00
MSFT| ₹420.00

Note: These are sample prices used by the program, not live market prices.

Technologies Used

- Python
- "os" module for file-related operations

Python Concepts Used

- Variables and dictionaries
- Functions
- Conditional statements
- Loops
- User input and validation
- Exception handling (invalid input, Ctrl+C, file errors)
- File handling

How to Run

1. Make sure Python is installed on your computer.
2. Open a terminal in the main repository folder.
3. Run the following command:

python Task-2-Stock-Portfolio/stock_portfolio.py

If your Python installation uses "python3", run:

python3 Task-2-Stock-Portfolio/stock_portfolio.py

How to Use

1. Run the program.
2. Select 1 to add a stock.
3. Enter a valid stock ticker, such as "AAPL".
4. Enter the number of shares.
5. Select 2 to view your portfolio and total value.
6. Select 3 to save your portfolio to "portfolio.txt".
7. Select 4 to exit the application.

Example

If you add 50 shares of AAPL at the sample price of ₹180 per share:

- Stock ticker: AAPL
- Number of shares: 50
- Sample price per share: ₹180
- Holding value: ₹9,000.00

Output File

The program saves portfolio details in "portfolio.txt" when the save option is selected.

AI Assistance

AI tools were used as a learning aid during development. The program was tested, and I am learning how its code works.

Internship

Program: Datheon Python Programming Internship
Task: Task 2 — Stock Portfolio Tracker
