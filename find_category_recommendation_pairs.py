# Amazon wants to understand shopping patterns across product categories. Write a solution to:
# Find all category pairs (where category1 < category2)
# For each category pair, determine the number of unique customers who purchased products from both categories
# A category pair is considered reportable if at least 3 different customers have purchased products from both categories.
# Return the result table of reportable category pairs ordered by customer_count in descending order, and in case of a tie, by category1 in ascending order lexicographically, and then by category2 in ascending order.
import pandas as pd


def find_category_recommendation_pairs(
    product_purchases: pd.DataFrame, product_info: pd.DataFrame
) -> pd.DataFrame:
    tab = pd.merge(
        product_purchases,
        product_info[["product_id", "category"]],
        how="inner",
        on="product_id",
    )
    tab = pd.merge(tab, tab, how="inner", on="user_id")
    tab = tab[["user_id", "category_x", "category_y"]].drop_duplicates()
    tab = tab.loc[tab["category_x"] < tab["category_y"]]
    tab = tab.groupby(["category_x", "category_y"])["user_id"].count().reset_index()
    tab = tab.loc[tab["user_id"] > 2].rename(
        columns={
            "category_x": "category1",
            "category_y": "category2",
            "user_id": "customer_count",
        }
    )
    return tab[["category1", "category2", "customer_count"]].sort_values(
        by=["customer_count", "category1", "category2"], ascending=[False, True, True]
    )
