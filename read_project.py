import pandas as pd

while True:
    
    user_input = input("press 1 for see the data or read the data\n"
                       "press 2 for convert the data and save\n"
                       "press 3 for do both:-\n"
                       "press exit to quit:- ").strip()

    if user_input == "1":
        df1 = str(input("Which file will you provide, CSV, Excel, or JSON?:- ")).lower().strip()
        
        if df1 == "csv":
            path = str(input("CSV FILE PATH:-")).strip()
            df = pd.read_csv(path, encoding="latin-1")
            print(df)
            
        elif df1 == "excel":
            path = str(input("EXCEL FILE PATH:-")).strip()
            df = pd.read_excel(path)
            print(df)
        
        elif df1 == "json":
            path = str(input("JSON FILE PATH:-")).strip()
            df = pd.read_json(path)
            print(df)
        
        else:
            print("Invalid file type. Please choose CSV, Excel, or JSON.")
    
    elif user_input == "2":
        
        df3 = str(input("Which file will you provide, CSV, Excel, or JSON?:- ")).lower().strip()
        
        if df3 == "csv":
            
            user_input3 = int(input("Type 1 to convert CSV to Excel\n"
                                    "Type 2 to convert CSV to JSON\n"))
            
            if user_input3  == 1:
                path = input("CSV FILE PATH:-").strip()
                df = pd.read_csv(path, encoding="latin-1")
                df.to_excel("updated output.xlsx", index=False)
            
            elif user_input3 == 2:
                path = input("CSV FILE PATH:-").strip()
                df = pd.read_csv(path, encoding="latin-1")
                df.to_json("updated output.json", index=False)
            
            else:
                print("Invalid option. Please choose 1 or 2.")
        
        elif df3 == "excel":
            user_input4 = int(input("Type 1 to convert Excel to CSV\n"
                                    "Type 2 to convert Excel to JSON\n"))
            
            if user_input4 == 1:
                path = input("EXCEL FILE PATH:-").strip()
                df = pd.read_excel(path)
                df.to_csv("updated output.csv", index=False)
            
            elif user_input4 == 2:
                path = input("EXCEL FILE PATH:-").strip()
                df = pd.read_excel(path)
                df.to_json("updated output.json", index=False)
            
            else:
                print("Invalid option. Please choose 1 or 2.")      
        
        elif df3 == "json":
                user_input5 = int(input("Type 1 to convert JSON to CSV\n"
                                    "Type 2 to convert JSON to Excel\n"))
            
                if user_input5 == 1:
                    path = input("JSON FILE PATH:-").strip()
                    df = pd.read_json(path)
                    df.to_csv("updated output.csv", index=False)
            
                elif user_input5 == 2:
                    path = input("JSON FILE PATH:-").strip()
                    df = pd.read_json(path)
                    df.to_excel("updated output.xlsx", index=False)
            
                else:
                    print("Invalid option. Please choose 1 or 2.")
    
    elif  user_input == "3":
        df4 = str(input("Which file will you provide, CSV, Excel, or JSON?:- ")).lower().strip()
        
        if df4 == "csv":
            path = input("CSV FILE PATH:-").strip()
            df = pd.read_csv(path, encoding="latin-1")
            print(df)
            user_input6 = int(input("Type 1 to convert CSV to Excel\n"
                                    "Type 2 to convert CSV to JSON\n"))
            
            if user_input6  == 1:
                df.to_excel("updated output.xlsx", index=False)
            
            elif user_input6 == 2:
                df.to_json("updated output.json", index=False)
            
            else:
                print("Invalid option. Please choose 1 or 2.")
        
        elif df4 == "excel":
            path = input("EXCEL FILE PATH:-").strip()
            df = pd.read_excel(path)
            print(df)
            user_input7 = int(input("Type 1 to convert Excel to CSV\n"
                                    "Type 2 to convert Excel to JSON\n"))
            
            if user_input7 == 1:
                df.to_csv("updated output.csv", index=False)
            
            elif user_input7 == 2:
                df.to_json("updated output.json", index=False)
            
            else:
                print("Invalid option. Please choose 1 or 2.")      
        
        elif df4 == "json":
            path = input("JSON FILE PATH:-").strip()
            df = pd.read_json(path)
            print(df)
            user_input8 = int(input("Type 1 to convert JSON to CSV\n"
                                    "Type 2 to convert JSON to Excel\n"))
            
            if user_input8 == 1:
                df.to_csv("updated output.csv", index=False)
            
            elif user_input8 == 2:
                df.to_excel("updated output.xlsx", index=False)
            
            else:
                print("Invalid option. Please choose 1 or 2.")    
    
    elif user_input == "exit":
        print("Exiting the program.")
        break
    
    else:
        print("Invalid input. Please choose 1, 2, 3, or type 'exit' to quit.")    
        
        
        
      
            

   
    
