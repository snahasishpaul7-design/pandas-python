import pandas as pd

data = {
    "ID": [1005, 1002, 1008, 1001, 1006, 1003],

    "Name": [
        "Hasan",
        "Karim",
        "Nayeem",
        "Rahim",
        "Sakib",
        "Tanvir"
    ],

    "Age": [
        25,
        21,
        24,
        20,
        23,
        22
    ]
}

df = pd.DataFrame(data)

print(df)
df.sort_values(by="Age",ascending=True,inplace=True)

df.sort_values(by=["Age","ID"],ascending=True,inplace=True)

print(df)