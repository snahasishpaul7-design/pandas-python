
import pandas as pd 
 
def show_row(df): 
 
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
 
 
def show_info(df): 
 
    data = input("Do you want to see the DataFrame info? (yes/no):-").lower().strip() 
 
    if data == "yes": 
 
        data1 = df.info() 
         
        print(data1) 
 
    elif data == "no": 
 
        print() 
 
 
def show_shape(df): 
 
    data = input("Do you want to see the DataFrame shape? (yes/no):-").lower().strip() 
 
    if data == "yes": 
 
        shape = df.shape 
 
        print(f"The DataFrame has {shape[0]} rows and {shape[1]} columns.") 
 
    elif data == "no": 
 
        print() 
 
 
def show_description_statistics(df): 
 
    data = input("Do you want to need mean, variance, max, 25%, 50%:- ").strip().lower() 
 
    if data == "yes": 
 
        des = df.describe() 
 
        print(des) 
 
    elif data == "no": 
 
        print() 
 
 
def column(df): 
     
    print(df) 
    
    user5 = input("Do you want to select column name:-").lower().strip()
    
    if user5 == "yes":
 
        user4 = int(input("How many columns do you want to select? ")) 
 
        columns = [] 
 
        for i in range(user4): 
 
            user = input(f"Enter the name of column {i + 1}: ").strip().upper()
        
            for col in df.column:
            
                if col.lower() == user.lower():
                
                    columns.append(user)
                
                    break
  
 
        user_input3 = df[columns] 
 
        print(user_input3) 
    
    elif user5 == "no":
        
        print()
    
    else:
        
        print("Invalid")
     
 
 
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
 
    df1 = str(input("Which file will you provide, CSV, Excel, or JSON?:- ")).lower().strip() 
 
    if df1 == "csv": 
 
        return read_csv() 
 
    elif df1 == "excel": 
 
        return read_excel() 
 
    elif df1 == "json": 
 
        return read_json() 
 
    else: 
 
        print("Invalid file type.") 
 
 
def read_care(): 
 
    df = read_data() 
 
 
def read_care2(): 
 
    df = read_data() 
 
    show_row(df) 
 
 
def read_care3(): 
 
    df = read_data() 
 
    show_info(df) 
 
 
def read_care4(): 
 
    df = read_data() 
 
    show_shape(df) 
 
 
def read_care5(): 
 
    df = read_data() 
 
    show_description_statistics(df) 
 
 
def read_ultra_care(): 
 
    df = read_data() 
 
    show_row(df) 
    show_shape(df) 
    show_info(df) 
    show_description_statistics(df) 
    column(df) 
 
 
def exit(): 
 
    quit() 
 
 
while True: 
 
    print( 
        "press 1 just to read the data\n" 
        "press 2 to show the data\n" 
        "press 3 to show the info of data\n" 
        "press 4 to show the shape of data\n" 
        "press 5 to show the statistics value of data\n" 
        "press 6 to show everything\n" 
        "press 7 to exit the program\n" 
        "press 8 to select the column" 
    ) 
 
    user_input4 = int(input("Which operation do you want to do:-")) 
 
    if user_input4 == 1: 
 
        read_data() 
 
    elif user_input4 == 2: 
 
        df = read_data() 
        show_row(df) 
 
    elif user_input4 == 3: 
 
        df = read_data() 
        show_info(df) 
 
    elif user_input4 == 4: 
 
        df = read_data() 
        show_shape(df) 
 
    elif user_input4 == 5: 
 
        df = read_data() 
        show_description_statistics(df) 
 
    elif user_input4 == 6: 
 
        read_ultra_care() 
 
    elif user_input4 == 7: 
 
        print("Quitting") 
 
        exit() 
     
    elif user_input4 == 8: 
         
        df = read_data()
        column(df) 
 
    else: 
 
        print("Invalid.........please give the input carefully")
