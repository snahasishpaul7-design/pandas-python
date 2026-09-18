import pandas as pd

df = pd.read_csv("sales_data_sample.csv",encoding = "latin-1")

print(df.head(5))

print(df.tail(6))