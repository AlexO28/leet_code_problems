# Amazon wants to implement the Customers who bought this also bought... feature based on co-purchase patterns. Write a solution to :
# Identify distinct product pairs frequently purchased together by the same customers (where product1_id < product2_id)
# For each product pair, determine how many customers purchased both products
# A product pair is considered for recommendation if at least 3 different customers have purchased both products.
# Return the result table ordered by customer_count in descending order, and in case of a tie, by product1_id in ascending order, and then by product2_id in ascending order.
import pandas as pd


def find_product_recommendation_pairs(
    product_purchases: pd.DataFrame, product_info: pd.DataFrame
) -> pd.DataFrame:
    tab = pd.merge(product_purchases, product_purchases, how="inner", on="user_id")
    tab = tab.loc[tab["product_id_x"] < tab["product_id_y"]][
        ["user_id", "product_id_x", "product_id_y"]
    ]
    tab = (
        tab.groupby(["product_id_x", "product_id_y"])["user_id"]
        .count()
        .reset_index()
        .rename(
            columns={
                "product_id_x": "product1_id",
                "product_id_y": "product2_id",
                "user_id": "customer_count",
            }
        )
    )
    tab = tab.loc[tab["customer_count"] > 2]
    tab = pd.merge(
        tab,
        product_info[["product_id", "category"]],
        how="inner",
        left_on="product1_id",
        right_on="product_id",
    ).rename(columns={"category": "product1_category"})
    del tab["product_id"]
    tab = pd.merge(
        tab,
        product_info[["product_id", "category"]],
        how="inner",
        left_on="product2_id",
        right_on="product_id",
    ).rename(columns={"category": "product2_category"})
    del tab["product_id"]
    return tab.sort_values(
        by=["customer_count", "product1_id", "product2_id"],
        ascending=[False, True, True],
    )[
        [
            "product1_id",
            "product2_id",
            "product1_category",
            "product2_category",
            "customer_count",
        ]
    ]
