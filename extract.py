import yfinance
import pandas as pd
import os
import glob

base_path = os.getcwd()
path = f"{base_path}/CSVs/raw_batch/*"

try:
    files = glob.glob(path)
    for f in files:
        os.remove(f)
except Exception as err:
    print(err)


df = yfinance.Ticker("AAPL").history(period="1y", interval="1d")

print(df.head())

df.to_csv("./CSVs/raw_batch/current_batch.csv", index=True)