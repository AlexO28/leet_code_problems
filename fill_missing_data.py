# Write a solution to fill in the missing value as 0 in the quantity column.
import pandas as pd

def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    products.loc[pd.isnull(products["quantity"]), "quantity"] = 0
    return products
