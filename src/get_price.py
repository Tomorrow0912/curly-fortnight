import yfinance as yf

def get_latest_close(symbol):
    try:
        symbol = input("Enter ticker: ")
        Ticker = yf.Ticker(symbol)
        history = Ticker.history(period="1d", interval="15m")
        if history.empty:
            return None
        latest_close = history["Close"].iloc[-1]
        return round(latest_close, 2)
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None
    
