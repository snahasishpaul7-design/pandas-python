#to fill any missing value with number
#fillna(value,inplace=True)

import pandas as pd

data = {
    "Name": ["Rahim", "Karim", "Sakib", "Nayeem", "Hasan"],
    "Age": [20, 21, None, 22, 20],
    "Department": ["CSE", "EEE", None, "CSE", "BBA"],
    "CGPA": [3.75, None, 3.50, 3.90, None],
    "City": ["Dhaka", "Narsingdi", "Dhaka", None, "Gazipur"]
}

df = pd.DataFrame(data)

print(df)

df["Age"]=df["Age"].fillna(0)
print(df)
df["CGPA"]=df["CGPA"].fillna(0) 
print(df)

df["Age"] = df["Age"].fillna(df["Age"].mean()) #Replace nan value with mean

print(df)