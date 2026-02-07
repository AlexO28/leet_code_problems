# Write a solution to find golden hour customers - customers who consistently order during peak hours and provide high satisfaction. A customer is a golden hour customer if they meet ALL the following criteria:# 
# Made at least 3 orders.
# At least 60% of their orders are during peak hours (11:00-14:00 or 18:00-21:00).
# Their average rating for rated orders is at least 4.0, round it to 2 decimal places.
# Have rated at least 50% of their orders.
# Return the result table ordered by average_rating in descending order, then by customer_id​​​​​​​ in descending order.
# The result format is in the following example.
import pandas as pd
from datetime import datetime


def find_golden_hour_customers(restaurant_orders: pd.DataFrame) -> pd.DataFrame:
    restaurant_orders["order_timestamp"] = restaurant_orders["order_timestamp"].apply(
        lambda x: datetime.strptime(x, "%Y-%m-%d %H:%M:%S")
    )
    restaurant_orders["metric"] = restaurant_orders["order_timestamp"].apply(
        lambda x: x.hour * 100 + x.minute
    )
    customers = (
        restaurant_orders[["customer_id"]].drop_duplicates().reset_index(drop=True)
    )
    customers["total_orders"] = -1
    customers["peak_hour_percentage"] = -1
    customers["average_rating"] = -1
    for j in range(len(customers)):
        tab = restaurant_orders.loc[
            restaurant_orders["customer_id"] == customers.loc[j, "customer_id"]
        ]
        if len(tab) < 3:
            continue
        num_peak = len(
            tab.loc[
                ((tab["metric"] >= 1100) & (tab["metric"] <= 1400))
                | ((tab["metric"] >= 1800) & (tab["metric"] <= 2100))
            ]
        )
        peak_hour_percentage = num_peak / len(tab)
        if peak_hour_percentage < 0.6:
            continue
        average_rating = round(
            tab.loc[~pd.isnull(tab["order_rating"]), "order_rating"].mean(), 2
        )
        if average_rating < 4:
            continue
        num_rated = len(tab.loc[~pd.isnull(tab["order_rating"])])
        if num_rated / len(tab) < 0.5:
            continue
        customers.loc[j, "total_orders"] = len(tab)
        customers.loc[j, "peak_hour_percentage"] = round(peak_hour_percentage * 100 + 0.0001)
        customers.loc[j, "average_rating"] = average_rating
    return customers.loc[customers["average_rating"] >= 0].sort_values(
        by=["average_rating", "customer_id"], ascending=False
    )
