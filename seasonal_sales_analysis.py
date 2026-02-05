# Write a solution to find the most popular product category for each season. The seasons are defined as:
# Winter: December, January, February
# Spring: March, April, May
# Summer: June, July, August
# Fall: September, October, November
# The popularity of a category is determined by the total quantity sold in that season. If there is a tie, select the category with the highest total revenue (quantity × price). If there is still a tie, return the lexicographically smaller category.
# Return the result table ordered by season in ascending order.
import pandas as pd


def seasonal_sales_analysis(
    products: pd.DataFrame, sales: pd.DataFrame
) -> pd.DataFrame:
    sales["month"] = sales["sale_date"].apply(lambda x: x.month)
    sales["season"] = "Winter"
    sales.loc[sales["month"].isin([3, 4, 5]), "season"] = "Spring"
    sales.loc[sales["month"].isin([6, 7, 8]), "season"] = "Summer"
    sales.loc[sales["month"].isin([9, 10, 11]), "season"] = "Fall"
    sales = sales[["season", "product_id", "quantity", "price"]]
    tab = pd.merge(sales, products, how="inner", on="product_id")
    tab["price"] = tab["price"] * tab["quantity"]
    tab = (
        tab.groupby(["season", "category"])
        .agg({"quantity": "sum", "price": "sum"})
        .reset_index()
        .rename(columns={"quantity": "total_quantity", "price": "total_revenue"})
    )
    tab_fall = (
        tab.loc[tab["season"] == "Fall"]
        .sort_values(by=["total_quantity", "total_revenue"], ascending=False)
        .head(1)
    )
    tab_spring = (
        tab.loc[tab["season"] == "Spring"]
        .sort_values(by=["total_quantity", "total_revenue"], ascending=False)
        .head(1)
    )
    tab_summer = (
        tab.loc[tab["season"] == "Summer"]
        .sort_values(by=["total_quantity", "total_revenue"], ascending=False)
        .head(1)
    )
    tab_winter = (
        tab.loc[tab["season"] == "Winter"]
        .sort_values(by=["total_quantity", "total_revenue"], ascending=False)
        .head(1)
    )
    return pd.concat(
        [tab_fall, tab_spring, tab_summer, tab_winter], axis=0
    ).sort_values(by="season")
