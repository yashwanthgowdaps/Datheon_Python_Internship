
# Task 2: Stock Portfolio Tracker

# Predefined sample prices (not live market prices)
stock_prices = {
    "AAPL": 180.00,
    "TSLA": 250.00,
    "GOOGL": 150.00,
    "MSFT": 420.00
}

portfolio = {}

print("===== STOCK PORTFOLIO TRACKER =====")
print("\nAvailable stocks and sample prices:")

for symbol, price in stock_prices.items():
    print(symbol, "- ₹", price)

while True:
    print("\n1. Add stock")
    print("2. View portfolio")
    print("3. Save portfolio to a text file")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ").strip()

    if choice == "1":
        symbol = input("Enter stock ticker: ").strip().upper()

        if symbol not in stock_prices:
            print("Stock not available. Choose a listed ticker.")
            continue

        try:
            quantity = int(input("Enter number of shares: "))

            if quantity <= 0:
                print("Shares must be greater than zero.")
                continue

        except ValueError:
            print("Please enter a valid whole number.")
            continue

        portfolio[symbol] = portfolio.get(symbol, 0) + quantity

        value = portfolio[symbol] * stock_prices[symbol]

        print("Stock added successfully!")
        print("Total shares of", symbol, ":", portfolio[symbol])
        print("Holding value: ₹", round(value, 2))

    elif choice == "2":
        if not portfolio:
            print("Your portfolio is empty.")
            continue

        total_value = 0

        print("\n===== YOUR PORTFOLIO =====")

        for symbol, quantity in portfolio.items():
            price = stock_prices[symbol]
            value = quantity * price
            total_value += value

            print("\nTicker:", symbol)
            print("Shares:", quantity)
            print("Sample price: ₹", price)
            print("Holding value: ₹", round(value, 2))

        print("\nTotal portfolio value: ₹", round(total_value, 2))

    elif choice == "3":
        if not portfolio:
            print("Add at least one stock before saving.")
            continue

        total_value = 0

        with open("portfolio.txt", "w") as file:
            file.write("STOCK PORTFOLIO REPORT\n")
            file.write("======================\n")

            for symbol, quantity in portfolio.items():
                price = stock_prices[symbol]
                value = quantity * price
                total_value += value

                file.write(
                    f"{symbol}: {quantity} shares x "
                    f"₹{price:.2f} = ₹{value:.2f}\n"
                )

            file.write(
                f"\nTotal portfolio value: ₹{total_value:.2f}\n"
            )

        print("Portfolio saved to portfolio.txt")

    elif choice == "4":
        print("Thank you for using Stock Portfolio Tracker!")
        break

    else:
        print("Invalid choice. Enter a number from 1 to 4.")
        