# Write a solution to find all products whose description contains a valid serial number pattern. A valid serial number follows these rules:
# It starts with the letters SN (case-sensitive).
# Followed by exactly 4 digits.
# It must have a hyphen (-) followed by exactly 4 digits.
# The serial number must be within the description (it may not necessarily start at the beginning).
# Return the result table ordered by product_id in ascending order.
import pandas as pd
import re


def find_valid_serial_products(products: pd.DataFrame) -> pd.DataFrame:
    products["valid"] = products["description"].apply(lambda x: is_valid(x))
    return products.loc[products["valid"] == True][
        ["product_id", "product_name", "description"]
    ].sort_values(by="product_id")


def is_valid(text):
    words = text.split(" ")
    for word in words:
        if re.fullmatch("SN\d{4}-\d{4}", word):
            return True
    return False
