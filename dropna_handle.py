#df.dropna(axis = 1 ,inplace = True) 1 is column and 0 is row

import pandas as pd

data = {
    "Name": ["Rahim", "Karim", "Sakib", "Nayeem", "Hasan"],
    "Age": [20, 21, None, 22, 20],
    "Department": ["CSE", "EEE", None, "CSE", "BBA"],
    "CGPA": [3.75, None, 3.50, 3.90, None],
    "City": ["Dhaka", "Narsingdi", "Dhaka", None, "Gazipur"]
}

df=pd.DataFrame(data)

#df.dropna(inplace=True)#delete all none values
df.dropna(subset=["Age"], inplace=True) #subset is mainly use for to  
#remove the exact  nan value of the column without not removing the whole column

print(df)

df.drop("Age", axis=1, inplace=True)

print(df)