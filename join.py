import pandas as pd


df1 = pd.DataFrame({
    "ID": [1, 2, 3, 4],
    "Name": ["Ananta", "Rahim", "Karim", "Sakib"]
})

df2 = pd.DataFrame({
    "ID": [3, 4, 5, 6],
    "Salary": [30000, 40000, 50000, 60000]
})


# 1. INNER JOIN
# Returns only the rows where the ID exists in both DataFrames.
inner_join = pd.merge(df1, df2, on="ID", how="inner")

print("INNER JOIN")
print(inner_join)


# 2. LEFT JOIN
# Returns all rows from the left DataFrame and matching rows from the right DataFrame.
left_join = pd.merge(df1, df2, on="ID", how="left")

print("\nLEFT JOIN")
print(left_join)


# 3. RIGHT JOIN
# Returns all rows from the right DataFrame and matching rows from the left DataFrame.
right_join = pd.merge(df1, df2, on="ID", how="right")

print("\nRIGHT JOIN")
print(right_join)


# 4. OUTER JOIN
# Returns all rows from both DataFrames and matches them where possible.
outer_join = pd.merge(df1, df2, on="ID", how="outer")

print("\nOUTER JOIN")
print(outer_join)


# 5. CROSS JOIN
# Creates every possible combination of rows from both DataFrames.
cross_join = pd.merge(df1, df2, how="cross")

print("\nCROSS JOIN")
print(cross_join)

# INNER = common data
