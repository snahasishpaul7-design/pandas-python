import pandas as pd


# ==========================================
# 1. LINEAR INTERPOLATION
# ==========================================

data1 = {
    "Value": [10, 20, None, 40, 50]
}

df1 = pd.DataFrame(data1)

print("BEFORE LINEAR:")
print(df1)

df1["Value"] = df1["Value"].interpolate(method="linear")

print("\nAFTER LINEAR:")
print(df1)


# ==========================================
# 2. POLYNOMIAL INTERPOLATION
# ==========================================

data2 = {
    "Value": [10, 20, None, 80, 160]
}

df2 = pd.DataFrame(data2)

print("\n\nBEFORE POLYNOMIAL:")
print(df2)

df2["Value"] = df2["Value"].interpolate(
    method="polynomial",
    order=3
)

print("\nAFTER POLYNOMIAL:")
print(df2)


# ==========================================
# 3. TIME INTERPOLATION
# ==========================================

data3 = {
    "Date": [
        "2026-01-01",
        "2026-01-02",
        "2026-01-03",
        "2026-01-04"
    ],
    "Temperature": [20, None, None, 30]
}

df3 = pd.DataFrame(data3)

df3["Date"] = pd.to_datetime(df3["Date"])

df3 = df3.set_index("Date")

print("\n\nBEFORE TIME:")
print(df3)

df3["Temperature"] = df3["Temperature"].interpolate(
    method="time"
)

print("\nAFTER TIME:")
print(df3)