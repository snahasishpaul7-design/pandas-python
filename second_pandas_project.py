import pandas as pd

def show_row():
    df = read_data()
    df1 = input("View top or bottom rows? (head/tail) yes or no:-").lower().strip()
    if df1 == "yes":
        df2 = input("Type head or tail:-").lower().strip()
        if df2 == "head":
            user_input1 = int(input("How many rows would you like to view from the top?:-"))
            print(df.head(user_input1))
        elif df2 == "tail":
            user_input2 = int(input("How many rows would you like to view from the bottom?:-"))
            print(df.tail(user_input2))
        else:
            print("Invalid input. Please enter 'head' or 'tail'.")
    elif df1 == "no":
        print()

def show_info():
    df = read_data()
    data = input("Do you want to see the DataFrame info? (yes/no):-").lower().strip()
    if data == "yes":
        df.info()
        
    elif data == "no":
        print()

def show_shape():
    df = read_data()
    data = input("Do you want to see the DataFrame shape? (yes/no):-").lower().strip()
    if data == "yes":
        shape = df.shape
        print(f"The DataFrame has {shape[0]} rows and {shape[1]} columns.")
    elif data == "no":
        print()

def show_description_statistics():
    df = read_data()
    data = input("Do you want to need mean, variance, max, 25%, 50%:- ").strip().lower()
    if data == "yes":
        des = df.describe()
        print(des)
    elif data == "no":
        print()

def add_new_column():
    df = read_data()
    Column_name = str(input("Enter the column name:-"))
    in_dx = int(input("Enter the index:-"))
    values = []
    for i in range(len(df)):
        val = input(f"Enter the Values {i + 1}:-")
        values.append(val)
    df.insert(in_dx, Column_name, values)
    print(df)

def column():
    df = read_data()
    print(df)
    print(list(df))
    user5 = input("Do you want to select column name:-").lower().strip()
    if user5 == "yes":
        user4 = int(input("How many columns do you want to select? "))
        columns = []
        for i in range(user4):
            user = input(f"Enter the name of column {i + 1}: ").strip().upper()
            for col in df.columns:
                if col.lower() == user.lower():
                    columns.append(col)
                    break
        user_input3 = df[columns]
        print(user_input3)
    elif user5 == "no":
        print()
    else:
        print("Invalid")

def null_value():
    df = read_data()
    print(df.isnull())
    nu_in = input("Do you want to see the sum of null values:-").lower().strip()
    if nu_in == "yes":
        print(df.isnull().sum())
    elif nu_in == "no":
        print()
    else:
        print("Invalid! type yes or no")

def delete_column():
    df = read_data()
    inp = input("Press 1 to delete entire row:-\npress 2 to delete the none value of the row:-")
    if inp == "1":
        user_in1 = int(input("Press 0 to delete row wise \npress 1 to delete column wise:-"))
        if user_in1 == 0:
            print("\nCurrent rows:")
            print(list(df.index))
            row = int(input("Which row you want to delete? "))
            if row in df.index:
                df.drop(row, axis=user_in1, inplace=True)
                print(df)
        elif user_in1 == 1:
            print("\nCurrent columns:")
            print(list(df.columns))
            column = input("Which column you want to delete?:- ")
            if column in df.columns:
                df.drop(column, axis=user_in1, inplace=True)
                print(df)
            else:
                print("Column not found")
        else:
            print("Invalid")
    elif inp == "2":
        print("\nCurrent columns:")
        print(list(df.columns))
        column = input("Which column missing value you want to delete?:- ")
        if column in df.columns:
            df.dropna(subset=[column], axis=0, inplace=True)
            print("Rows with missing values deleted successfully.")
            print(df)
        else:
            print("Column not found")
    else:
        print("Invalid")

def sort():
    df = read_data()
    print("\nAvailable columns:")
    print(list(df.columns))
    number = int(input("\nHow many columns do you want to sort by? "))
    columns = []
    for i in range(number):
        column = input(f"Enter column {i + 1}: ")
        columns.append(column)
    print("\nSelected columns:", columns)
    df.sort_values(by=columns, ascending=True, inplace=True)
    print("\nAfter sorting:")
    print(df)

def read_csv():
    path = str(input("CSV FILE PATH:-")).strip()
    df = pd.read_csv(path, encoding="latin-1")
    print(df)
    return df

def read_excel():
    path = str(input("EXCEL FILE PATH:-")).strip()
    df = pd.read_excel(path)
    print(df)
    return df

def read_json():
    path = str(input("JSON FILE PATH:-")).strip()
    df = pd.read_json(path)
    print(df)
    return df

def read_data():
    while True:
        df1 = str(input("Which file will you provide, CSV, Excel, or JSON?:- ")).lower().strip()
        if df1 == "csv":
            return read_csv()
        elif df1 == "excel":
            return read_excel()
        elif df1 == "json":
            return read_json()
        else:
            print("Invalid file type.")

def concat():
    df = read_data()
    col2 = int(input("How many column you want to concat:-"))
    con = []
    for i in range(col2):
        col1 = input(f"Enter the column names{i+1}:-").split()
        con.append(df[col1])
    res = pd.concat(con, ignore_index=True)
    print(res)

def every():
    df = read_data()
    while True:
        print("\npress 1 to show the data\n"
              "press 2 to show the info\n"
              "press 3 to show the shape\n"
              "press 4 to show statistics\n"
              "press 5 to select column\n"
              "press 6 to add new column\n"
              "press 7 to sort column values\n"
              "press 8 to see null values\n"
              "press 9 to delete row or column\n"
              "press 10 to concat\n"
              "press 11 to show the statistics value of data\n"
              "Press 12 to use sorting\n")
        user = input("Which operation do you want to do:- ").strip()
        if user == "1":
            print(df)
        elif user == "2":
            data = input("Do you want to see the DataFrame info? (yes/no):- ").lower().strip()
            if data == "yes":
                df.info()
            elif data == "no":
                print()
            else:
                print("Invalid")
        elif user == "3":
            data = input("Do you want to see the DataFrame shape? (yes/no):- ").lower().strip()
            if data == "yes":
                shape = df.shape
                print(f"The DataFrame has {shape[0]} rows and {shape[1]} columns.")
            elif data == "no":
                print()
            else:
                print("Invalid")
        elif user == "4":
            data = input("Do you want to see the statistics? (yes/no):- ").lower().strip()
            if data == "yes":
                print(df.describe())
            elif data == "no":
                print()
            else:
                print("Invalid")
        elif user == "5":
            print("\nCurrent columns:")
            print(list(df.columns))
            user5 = input("Do you want to select column name? (yes/no):- ").lower().strip()
            if user5 == "yes":
                user4 = int(input("How many columns do you want to select? "))
                columns = []
                for i in range(user4):
                    column = input(f"Enter the name of column {i + 1}: ").strip()
                    for col in df.columns:
                        if col.lower() == column.lower():
                            columns.append(col)
                            break
                print(df[columns])
            elif user5 == "no":
                print()
            else:
                print("Invalid")
        elif user == "6":
            print("Warning: For small data use this, For large data, you must enter values for every row, or the column will not be added.")
            user_in2 = input("Do wou want to use this:-").strip().lower()
            if user_in2 == "yes":
                Column_name = input("Enter the column name:- ")
                in_dx = int(input("Enter the index:- "))
                values = []
                for i in range(len(df)):
                    val = input(f"Enter the Values {i + 1}:- ")
                    values.append(val)
                df.insert(in_dx, Column_name, values)
                print(df)
            elif user_in2 == "no":
                print()
            else:
                print("Invalid")
        elif user == "7":
            print("\nAvailable columns:")
            print(list(df.columns))
            number = int(input("\nHow many columns do you want to sort by? "))
            columns = []
            for i in range(number):
                column = input(f"Enter column {i + 1}: ").strip()
                columns.append(column)
            print("\nSelected columns:", columns)
            df.sort_values(by=columns, ascending=True, inplace=True)
            print("\nAfter sorting:")
            print(df)
        elif user == "8":
            print(df.isnull())
            nu_in = input("Do you want to see the sum of null values? ").lower().strip()
            if nu_in == "yes":
                print(df.isnull().sum())
            elif nu_in == "no":
                print()
            else:
                print("Invalid")
        elif user == "9":
            inp = input("Press 1 to delete entire row/column:-\nPress 2 to delete rows with none value:- ")
            if inp == "1":
                user_in1 = int(input("Press 0 to delete row wise\nPress 1 to delete column wise:- "))
                if user_in1 == 0:
                    print("\nCurrent rows:")
                    print(list(df.index))
                    row = int(input("Which row you want to delete? "))
                    if row in df.index:
                        df.drop(row, axis=user_in1, inplace=True)
                        print(df)
                    else:
                        print("Row not found")
                elif user_in1 == 1:
                    print("\nCurrent columns:")
                    print(list(df.columns))
                    column = input("Which column you want to delete?:- ")
                    if column in df.columns:
                        df.drop(column, axis=user_in1, inplace=True)
                        print(df)
                    else:
                        print("Column not found")
                else:
                    print("Invalid")
            elif inp == "2":
                print("\nCurrent columns:")
                print(list(df.columns))
                column = input("Which column missing value you want to delete?:- ")
                if column in df.columns:
                    df.dropna(subset=[column], axis=0, inplace=True)
                    print("Column's missing rows deleted successfully")
                    print(df)
                else:
                    print("Column not found")
            else:
                print("Invalid")
        elif user == "10":
            df = read_data()
            col2 = int(input("How many column you want to concat:-"))
            con = []
            for i in range(col2):
                col1 = input(f"Enter the column names{i+1}:-").split()
                con.append(df[col1])
            res = pd.concat(con, ignore_index=True)
            print(res)
        elif user == "11":
            data = input("Do you want to need mean, variance, max, 25%, 50%:- ").strip().lower()
            if data == "yes":
                des = df.describe()
                print(des)
            elif data == "no":
                print()
        elif user == "12":
            print("\nAvailable columns:")
            print(list(df.columns))
            number = int(input("\nHow many columns do you want to sort by? "))
            columns = []
            for i in range(number):
                column = input(f"Enter column {i + 1}: ")
                columns.append(column)
            print("\nSelected columns:", columns)
            df.sort_values(by=columns, ascending=True, inplace=True)
            print("\nAfter sorting:")
            print(df)

def read_care():
    read_data()

def read_care2():
    show_row()

def read_care3():
    show_info()

def read_care4():
    show_shape()

def read_care5():
    show_description_statistics()

def read_care6():
    add_new_column()

def read_ultra_care():
    every()

def exit():
    quit()

while True:
    print("press 1 just to read the data\n"
          "press 2 to show the data\n"
          "press 3 to show the info of data\n"
          "press 4 to show the shape of data\n"
          "press 5 to show the statistics value of data\n"
          "press 6 to show everything\n"
          "press 7 to exit the program\n"
          "press 8 to select the column\n"
          "press 9 to add new column\n"
          "press 0 to see the null values\n"
          "Press 11 to delete values\n"
          "press 12 to sort column values\n"
          "press 13 to conacat\n")
    user_input4 = int(input("Which operation do you want to do:-"))
    if user_input4 == 1:
        read_data()
    elif user_input4 == 2:
        read_care2()
    elif user_input4 == 3:
        read_care3()
    elif user_input4 == 4:
        read_care4()
    elif user_input4 == 5:
        show_description_statistics()
    elif user_input4 == 6:
        read_ultra_care()
    elif user_input4 == 7:
        print("Quitting")
        exit()
    elif user_input4 == 8:
        column()
    elif user_input4 == 9:
        read_care6()
    elif user_input4 == 0:
        null_value()
    elif user_input4 == 11:
        delete_column()
    elif user_input4 == 12:
        sort()
    elif user_input4 == 13:
        concat()
    else:
        print("Invalid.........please give the input carefully")
