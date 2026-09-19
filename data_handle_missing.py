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

print(df.isnull())

print(df.isnull().sum())