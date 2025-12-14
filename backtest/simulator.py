def run_backtest(df, signals):
    in_position = False
    trades = []
    entry_price = 0

    for i in range(len(df)):
        if signals["entry"].iloc[i] and not in_position:
            in_position = True
            entry_price = df["close"].iloc[i]
            entry_date = df.index[i]

        elif signals["exit"].iloc[i] and in_position:
            exit_price = df["close"].iloc[i]
            exit_date = df.index[i]
            trades.append(exit_price - entry_price)
            in_position = False

    total_return = sum(trades)
    return {
        "trades": len(trades),
        "total_return": total_return
    }
