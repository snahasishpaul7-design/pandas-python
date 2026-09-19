import pandas as pd

data = {
    "Student_ID": [
        1001, 1002, 1003, 1004, 1005,
        1006, 1007, 1008, 1009, 1010,
        1011, 1012, 1013, 1014, 1015,
        1016, 1017, 1018, 1019, 1020
    ],

    "Name": [
        "Rahim", "Karim", "Hasan", "Nadia", "Sadia",
        "Fahim", "Tanvir", "Mim", "Sakib", "Rafi",
        "Jannat", "Nayeem", "Tania", "Arif", "Sumaiya",
        "Shuvo", "Mehedi", "Nusrat", "Rakib", "Ayesha"
    ],

    "Age": [
        20, 21, 19, 22, 20,
        21, 23, 19, 20, 22,
        21, 20, 23, 19, 22,
        21, 20, 23, 19, 21
    ],

    "Department": [
        "CSE", "EEE", "CSE", "BBA", "CSE",
        "EEE", "BBA", "CSE", "EEE", "CSE",
        "BBA", "CSE", "EEE", "BBA", "CSE",
        "EEE", "CSE", "BBA", "EEE", "CSE"
    ],

    "Semester": [
        4, 6, 2, 8, 4,
        6, 8, 2, 4, 6,
        8, 4, 6, 2, 8,
        4, 6, 8, 2, 4
    ],

    "Marks": [
        85, 72, 91, 68, 78,
        88, 65, 95, 74, 82,
        69, 90, 76, 81, 87,
        70, 93, 66, 79, 84
    ],

    "Attendance": [
        92, 85, 96, 78, 88,
        94, 72, 97, 81, 89,
        75, 95, 86, 90, 93,
        80, 98, 70, 84, 91
    ],

    "City": [
        "Dhaka", "Narsingdi", "Comilla", "Dhaka", "Sylhet",
        "Chittagong", "Rajshahi", "Dhaka", "Khulna", "Narsingdi",
        "Dhaka", "Sylhet", "Comilla", "Rajshahi", "Dhaka",
        "Khulna", "Narsingdi", "Dhaka", "Sylhet", "Comilla"
    ],

    "Study_Hours": [
        5, 3, 6, 2, 4,
        5, 2, 7, 3, 5,
        2, 6, 4, 5, 6,
        3, 7, 2, 4, 5
    ]
}

df = pd.DataFrame(data)

df.loc[0,'Study_Hours'] = 20
df.loc[[0, 2, 4], ["Marks", "Attendance"]] = 100

df["Attendance"] = df["Attendance"]+1
print(df)