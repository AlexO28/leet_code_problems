# Write a solution to find stores that have inventory imbalance - stores where the most expensive product has lower stock than the cheapest product.
# For each store, identify the most expensive product (highest price) and its quantity
# For each store, identify the cheapest product (lowest price) and its quantity
# A store has inventory imbalance if the most expensive product's quantity is less than the cheapest product's quantity
# Calculate the imbalance ratio as (cheapest_quantity / most_expensive_quantity)
# Round the imbalance ratio to 2 decimal places
# Only include stores that have at least 3 different products
# Return the result table ordered by imbalance ratio in descending order, then by store name in ascending order.
# The result format is in the following example.
import pandas as pd


def find_inventory_imbalance(
    stores: pd.DataFrame, inventory: pd.DataFrame
) -> pd.DataFrame:
    stores["most_exp_product"] = ""
    stores["cheapest_product"] = ""
    stores["imbalance_ratio"] = -1
    for j in range(len(stores)):
        tab = inventory.loc[inventory["store_id"] == stores.loc[j, "store_id"]]
        print(tab)
        if len(tab) < 3:
            continue
        max_price = tab["price"].max()
        min_price = tab["price"].min()
        max_product = list(tab.loc[tab["price"] == max_price, "inventory_id"].values)[0]
        min_product = list(tab.loc[tab["price"] == min_price, "inventory_id"].values)[0]
        max_quantity = list(
            tab.loc[tab["inventory_id"] == max_product, "quantity"].values
        )[0]
        min_quantity = list(
            tab.loc[tab["inventory_id"] == min_product, "quantity"].values
        )[0]
        if max_quantity >= min_quantity:
            continue
        max_name = list(
            tab.loc[tab["inventory_id"] == max_product, "product_name"].values
        )[0]
        min_name = list(
            tab.loc[tab["inventory_id"] == min_product, "product_name"].values
        )[0]
        imbalance_ratio = round(min_quantity / max_quantity, 2)
        stores.loc[j, "most_exp_product"] = max_name
        stores.loc[j, "cheapest_product"] = min_name
        stores.loc[j, "imbalance_ratio"] = imbalance_ratio
    return stores.loc[stores["imbalance_ratio"] > 0].sort_values(
        by=["imbalance_ratio", "store_name"], ascending=[False, True]
    )
