# Write a solution to find all customers who never order anything.

import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    orders = orders["customerId"].drop_duplicates().values.tolist()
    customers = customers[~customers["id"].isin(orders)]
    customers = customers[["name"]]
    return customers.rename(columns = {"name": "Customers"})
