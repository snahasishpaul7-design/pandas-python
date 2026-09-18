import pandas as pd

df = pd.read_csv("sales_data_sample.csv", encoding="latin-1")

data = df.info()  #find non null values, data types, and memory usage of the DataFrame

print(data)