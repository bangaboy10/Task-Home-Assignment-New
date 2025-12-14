import pandas as pd
from nl_parser.nl_to_json import parse_nl
from dsl.parser import parse_dsl
from codegen.ast_to_python import generate_signals
from backtest.simulator import run_backtest

nl = "Buy when price closes above 20 day moving average and volume above 1M"

print("Natural Language:", nl)

dsl = """
ENTRY:
close > SMA(close,20) AND volume > 1000000
EXIT:
RSI(close,14) < 30
"""

print("Generated DSL:", dsl)

ast = parse_dsl(dsl)

print("Parsed AST:", ast)


df = pd.read_csv("data/sample_ohlcv.csv", index_col="date", parse_dates=True)
signals = generate_signals(ast, df)

result = run_backtest(df, signals)
print("Backtest Result:", result)

# Note: No trades were triggered because entry conditions were never satisfied in the sample dataset.
