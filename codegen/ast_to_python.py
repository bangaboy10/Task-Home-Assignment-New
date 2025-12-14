import pandas as pd

def generate_signals(ast, df):
    signals = pd.DataFrame(index=df.index)
    signals["entry"] = False
    signals["exit"] = False

    signals["entry"] = (
        df["close"] > df["close"].rolling(20).mean()
    ) & (df["volume"] > 1000000)

    signals["exit"] = df["close"].rolling(14).mean() < 30

    return signals
