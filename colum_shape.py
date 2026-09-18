import pandas as pd

df = pd.read_csv("sales_data_sample.csv", encoding="latin-1")

data = df.shape  #find the number of rows and columns in the DataFrame

data2 = df.columns  #find the column names of the DataFrame
print(data)

print(data2)