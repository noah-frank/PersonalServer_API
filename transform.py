import os
import glob
import pandas as pd
import pandas_ta as ta
base_path = f"{os.getcwd()}/CSVs"
raw_batch = f"{base_path}/raw_batch/current_batch.csv"
transformed_batch = f"{base_path}/transformed_batch"

try:
    files = glob.glob(f"{transformed_batch}/*")
    for f in files:
        os.remove(f)
except Exception as err:
    print(err)

df = pd.read_csv(raw_batch)

### TRANSFORMATIONS

df = df.drop(columns=["Dividends", "Stock Splits"])
df.columns = ["datetime", "open", "high", "low", "close", "volume", "ticker"]
df["datetime"] = pd.to_datetime(df["datetime"], utc=True)


df["SMA10"] = ta.sma(df.close, length=10)
df["SMA20"] = ta.sma(df.close, length=20)
df["SMA30"] = ta.sma(df.close, length=30)
df["AO"] = ta.ao(high=df.high, low=df.low)

ichimoku_df = ta.ichimoku(
    high=df['high'],
    low=df['low'],
    close=df['close'],
    include_chikou=False,
    lookahead=False
)[0]

df = pd.concat([df, ichimoku_df], axis=1)

df = df.dropna()
df = df.set_index("datetime", drop=True)

print(df.info())
print(df.index.name)

df.to_csv(f"{transformed_batch}/current_batch.csv")
