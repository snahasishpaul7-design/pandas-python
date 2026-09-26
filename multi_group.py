import pandas as pd

data = {
    
    "Name":["Sajib" , "Rakib" , "Pulok" , 'Marun' ,  'Narun'],
    
    "Age" : [28,32,22,32,28],
    
    "performance" : [10,6,9,5,7],
    
    "Salary": [50000,60000,45000,52000,480000 ]

}

df = pd.DataFrame(data)
print(df)

grouped = df.groupby(["Age","Salary"])['performance'].sum() #take unique value and sum 

# in age 32 comes 2 times so so in salary the sum will 60000+52000=112000

print(grouped)
