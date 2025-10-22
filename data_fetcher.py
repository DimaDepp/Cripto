import ccxt
import pandas as pd
from config import EXCHANGE

exchange = getattr(ccxt, EXCHANGE)()

def get_ohlcv(symbol="BTC/USDT", timeframe="15m", limit=100):
    data = exchange.fetch_ohlcv(symbol, timeframe=timeframe, limit=limit)
    df = pd.DataFrame(data, columns=["time", "open", "high", "low", "close", "volume"])
    df["close"] = df["close"].astype(float)
    return df
