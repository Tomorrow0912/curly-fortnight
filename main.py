from src import config
from src.get_price import get_latest_close

def main():
    # Ask user for ticker symbol, or use default
    symbol = input(f"Enter ticker symbol (default: {config.DEFAULT_TICKER}): ").strip()
    if not symbol:
        symbol = config.DEFAULT_TICKER

    price = get_latest_close(symbol.upper())

    if price is None:
        print("Failed to fetch price. Please try again.")
    else:
        print(f"Latest close price for {symbol}: {price:.2f}")

        # Example usage of threshold from config
        if price > config.PRICE_ALERT_THRESHOLD:
            print(f"⚠️ Alert: {symbol} price is above {config.PRICE_ALERT_THRESHOLD}!")

if __name__ == "__main__":
    main()