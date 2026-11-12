# Task 2: Stock Portfolio Performance Tracker

A console application that tracks stock holdings, calculates performance against what you paid, and saves the results to a CSV file.

## Features

- Add stocks by ticker, number of shares and **buy price**
- Buying the same stock again updates the average buy price
- Looks up the current price from a sample price table
- Calculates, for each holding: invested amount, market value, gain/loss and **gain/loss %**
- Calculates total invested, total value and overall gain/loss %
- Automatically writes **`portfolio_summary.csv`** after every change, and on exit or on request (menu option 3)
- Validates tickers, share counts and prices

## Sample Prices

Prices are sample data, not live market prices.

| Ticker | Price |
|--------|-------|
| AAPL | ₹180.00 |
| TSLA | ₹250.00 |
| GOOGL | ₹150.00 |
| MSFT | ₹420.00 |
| AMZN | ₹175.00 |
| NVDA | ₹480.00 |

To use more tickers, add a `sample_prices.csv` file next to `portfolio.py` with the columns `ticker,price`.

## How to Run

```
python Task-2-Stock-Portfolio/portfolio.py
```

## Example

Buy 10 AAPL at ₹150 and 5 AAPL at ₹200 (average buy ₹166.67). The current price is ₹180:

```
AAPL  (15 shares)
  Average buy price : ₹166.67
  Current price     : ₹180.00
  Invested          : ₹2,500.00
  Market value      : ₹2,700.00
  Gain / Loss       : ₹200.00 (+8.00%)
```

## Output File: `portfolio_summary.csv`

```
Ticker,Shares,Avg Buy Price,Current Price,Invested,Market Value,Gain/Loss,Gain/Loss %
AAPL,15,166.67,180.00,2500.00,2700.00,200.00,8.00
TOTAL,,,,2500.00,2700.00,200.00,8.00
```

## Python Concepts Used

Dictionaries, functions, loops, input validation, exception handling, and file handling with the built-in `csv` module.
