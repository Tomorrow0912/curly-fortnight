import yfinance as yf
symbol = input("Enter ticker: ")
Ticker = yf.Ticker(symbol)
history = Ticker.history(period="1d", interval="15m")
latest_close = history["Close"].iloc[-1]
print(f"Latest close price: {latest_close:.2f}")
#testing