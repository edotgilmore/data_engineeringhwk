import sys
print("Hello from data-engineering-hw1!")
print("arguments", sys.argv)

day = int(sys.argv[1]) if len(sys.argv) > 1 else 1
print(f"Running pipeline for day {day}")

print( "Pipeline execution completed." )

import pandas as pd

df = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
print(df.head())

df.to_parquet(f"output_day_{sys.argv[1]}.parquet")