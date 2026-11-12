# Task 2: Stock Portfolio Performance Tracker
# Datheon Python Programming Internship

import csv
import os

# Sample "current" prices (not live market data). If a file named
# sample_prices.csv (columns: ticker,price) sits next to this script,
# its prices are added to / override the ones below.
SAMPLE_PRICES = {
    "AAPL": 180.0,
    "TSLA": 250.0,
    "GOOGL": 150.0,
    "MSFT": 420.0,
    "AMZN": 175.0,
    "NVDA": 480.0,
}

CURRENCY = "₹"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SUMMARY_FILE = os.path.join(BASE_DIR, "portfolio_summary.csv")
PRICE_FILE = os.path.join(BASE_DIR, "sample_prices.csv")

# ticker -> {"shares": total shares, "cost": total amount invested}
portfolio = {}


def money(amount):
    sign = "-" if amount < 0 else ""
    return f"{sign}{CURRENCY}{abs(amount):,.2f}"


def load_prices():
    """Return the price table, merging in sample_prices.csv if present."""
    prices = dict(SAMPLE_PRICES)
    try:
        with open(PRICE_FILE, newline="", encoding="utf-8") as file:
            for row in csv.DictReader(file):
                try:
                    prices[row["ticker"].strip().upper()] = float(row["price"])
                except (KeyError, ValueError, AttributeError):
                    continue
    except OSError:
        pass
    return prices


PRICES = load_prices()


def read_positive(prompt, cast):
    """Ask for a positive number; return None if the input is invalid."""
    try:
        value = cast(input(prompt).strip())
    except ValueError:
        print("Invalid number. Please try again.")
        return None
    if value <= 0:
        print("The value must be greater than zero.")
        return None
    return value


def show_prices():
    print("\nAvailable stocks and current sample prices:")
    for ticker, price in PRICES.items():
        print(f"  {ticker:<6} {money(price)}")


def add_stock():
    show_prices()
    ticker = input("\nEnter stock ticker: ").strip().upper()
    if ticker not in PRICES:
        print("Stock not available. Choose a listed ticker.")
        return

    shares = read_positive("Enter number of shares: ", int)
    if shares is None:
        return
    buy_price = read_positive(f"Enter buy price per share ({CURRENCY}): ", float)
    if buy_price is None:
        return

    holding = portfolio.setdefault(ticker, {"shares": 0, "cost": 0.0})
    holding["shares"] += shares
    holding["cost"] += shares * buy_price

    print(f"\nAdded {shares} share(s) of {ticker} at {money(buy_price)}.")
    write_summary(quiet=True)  # automatic logging after every change


def build_rows():
    """Calculate value and gain/loss for every holding."""
    rows = []
    for ticker, holding in portfolio.items():
        shares = holding["shares"]
        cost = holding["cost"]
        current_price = PRICES[ticker]
        value = shares * current_price
        gain = value - cost
        percent = (gain / cost * 100) if cost else 0.0
        rows.append({
            "ticker": ticker,
            "shares": shares,
            "avg_buy": cost / shares,
            "current": current_price,
            "cost": cost,
            "value": value,
            "gain": gain,
            "percent": percent,
        })
    return rows


def totals(rows):
    cost = sum(r["cost"] for r in rows)
    value = sum(r["value"] for r in rows)
    gain = value - cost
    percent = (gain / cost * 100) if cost else 0.0
    return cost, value, gain, percent


def view_portfolio():
    rows = build_rows()
    print("\n===== YOUR PORTFOLIO =====")
    if not rows:
        print("Your portfolio is empty.")
        return

    for r in rows:
        print(f"\n{r['ticker']}  ({r['shares']} shares)")
        print(f"  Average buy price : {money(r['avg_buy'])}")
        print(f"  Current price     : {money(r['current'])}")
        print(f"  Invested          : {money(r['cost'])}")
        print(f"  Market value      : {money(r['value'])}")
        print(f"  Gain / Loss       : {money(r['gain'])} ({r['percent']:+.2f}%)")

    cost, value, gain, percent = totals(rows)
    print("\n----- TOTAL -----")
    print(f"Total invested : {money(cost)}")
    print(f"Total value    : {money(value)}")
    print(f"Gain / Loss    : {money(gain)} ({percent:+.2f}%)")


def write_summary(quiet=False):
    """Save the performance summary to portfolio_summary.csv."""
    rows = build_rows()
    try:
        with open(SUMMARY_FILE, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([
                "Ticker", "Shares", "Avg Buy Price", "Current Price",
                "Invested", "Market Value", "Gain/Loss", "Gain/Loss %",
            ])
            for r in rows:
                writer.writerow([
                    r["ticker"], r["shares"], f"{r['avg_buy']:.2f}",
                    f"{r['current']:.2f}", f"{r['cost']:.2f}",
                    f"{r['value']:.2f}", f"{r['gain']:.2f}",
                    f"{r['percent']:.2f}",
                ])
            if rows:
                cost, value, gain, percent = totals(rows)
                writer.writerow([
                    "TOTAL", "", "", "", f"{cost:.2f}", f"{value:.2f}",
                    f"{gain:.2f}", f"{percent:.2f}",
                ])
        if not quiet:
            print(f"Portfolio summary saved to {SUMMARY_FILE}")
    except OSError as error:
        print(f"Could not save portfolio summary: {error}")


def main():
    print("===== STOCK PORTFOLIO TRACKER =====")
    show_prices()

    while True:
        print("\n1. Add stock")
        print("2. View portfolio")
        print("3. Save summary to portfolio_summary.csv")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            add_stock()
        elif choice == "2":
            view_portfolio()
        elif choice == "3":
            write_summary()
        elif choice == "4":
            write_summary(quiet=True)
            print("Thank you for using Stock Portfolio Tracker!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")


if __name__ == "__main__":
    try:
        main()
    except (EOFError, KeyboardInterrupt):
        print("\nExiting. Goodbye!")
