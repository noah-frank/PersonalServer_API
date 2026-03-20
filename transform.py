import pandas as pd
import os
import glob

base_path = f"{os.getcwd()}/CSVs"
raw_batch = f"{base_path}/raw_batch"
transformed_batch = f"{base_path}/transformed_batch/*"

try:
    files = glob.glob(path)
    for f in files:
        os.remove(f)
except Exception as err:
    print(err)

pd.read_csv("")