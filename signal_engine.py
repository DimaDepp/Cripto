from core.data_fetcher import get_ohlcv
from strategies.ema_strategy import check_ema_signal
from strategies.rsi_strategy import check_rsi_signal

def analyze(symbol="BTC/USDT", interval="15m"):
    df = get_ohlcv(symbol, interval)
    ema_signal = check_ema_signal(df)
    rsi_signal = check_rsi_signal(df)

    result = f"📊 Анализ {symbol} ({interval})\n"
    if ema_signal:
        result += f"{ema_signal}\n"
    if rsi_signal:
        result += f"{rsi_signal}\n"
    if not ema_signal and not rsi_signal:
        result += "❌ Сигналов нет."
    return result
