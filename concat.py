import pandas as pd


df1 = pd.DataFrame({
    "ID": [1, 2, 3],
    "Name": ["Ananta", "Rahim", "Karim"]
})

df2 = pd.DataFrame({
    "ID": [4, 5, 6],
    "Name": ["Sakib", "Hasan", "Rafi"]
})


# 1. Row-wise Concatenation
# Adds the rows of df2 below the rows of df1.
row_concat = pd.concat([df1, df2], axis=0, ignore_index=True)

print("ROW-WISE CONCATENATION")
print(row_concat)


# 2. Column-wise Concatenation
# Adds the columns of df2 beside the columns of df1.
column_concat = pd.concat([df1, df2], axis=1)

print("\nCOLUMN-WISE CONCATENATION")
print(column_concat)
