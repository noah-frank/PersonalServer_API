import yfinance
import pandas as pd
import os
import glob
from datetime import datetime
import pytz

base_path = os.getcwd()
path = f"{base_path}/CSVs/raw_batch/*"

try:
    files = glob.glob(path)
    for f in files:
        os.remove(f)
except Exception as err:
    print(err)

start = datetime(2016, 3, 19, tzinfo=pytz.utc)
end = datetime(2026, 3, 19, tzinfo=pytz.utc)

ticker = "AAPL"
df = yfinance.Ticker(ticker).history(start=start, end=end, interval="1d")
df["Ticker"] = ticker

print(df.head())

df.to_csv("./CSVs/raw_batch/current_batch.csv", index=True)