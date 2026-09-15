import pandas as pd

data = [
    {
        "product_id": 101,
        "product": "Laptop",
        "category": "Electronics",
        "price": 850.50,
        "quantity": 5,
        "rating": 4.5
    }
]
df = pd.DataFrame(data)
df.to_excel("save_To.xlsx", index=False) #index false means it will not save the index column in the excel file

#to_excel is used to save the data in excel file format. You can use this function to save the data in excel file format.   

