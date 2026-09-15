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
dd = pd.DataFrame(data)

dd.to_csv("save_To.csv", index=False) #index false means it will not save the index column in the csv file

#to_csv is used to save the data in csv file format. You can use this function to save the data in csv file format.