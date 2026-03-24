
import os
import pandas as pd
from sqlalchemy import create_engine

base_path = f"{os.getcwd()}/CSVs"
transformed_batch = f"{base_path}/transformed_batch/current_batch.csv"

engine = create_engine("sqlite:///databases/stock_data.db", echo=True)

df = pd.read_csv(transformed_batch)
df.to_sql("Ticker", con=engine, if_exists="append", index=False)


