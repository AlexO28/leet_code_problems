# Write a solution to find loyal customers. A customer is considered loyal if they meet ALL the following criteria:
# Made at least 3 purchase transactions.
# Have been active for at least 30 days.
# Their refund rate is less than 20% .
# Refund rate is the proportion of transactions that are refunds, calculated as the number of refund transactions divided by the total number of transactions (purchases plus refunds).
# Return the result table ordered by customer_id in ascending order.
import pandas as pd
from datetime import datetime


def find_loyal_customers(customer_transactions: pd.DataFrame) -> pd.DataFrame:
    customer_transactions["transaction_date"] = customer_transactions[
        "transaction_date"
    ].apply(lambda x: datetime.strptime(x, "%Y-%m-%d"))
    customers = (
        customer_transactions[["customer_id"]].drop_duplicates().reset_index(drop=True)
    )
    res = []
    for j in range(len(customers)):
        tab = customer_transactions.loc[
            customer_transactions["customer_id"] == customers.loc[j, "customer_id"]
        ]
        if len(tab) < 3:
            continue
        date_min = tab["transaction_date"].min()
        date_max = tab["transaction_date"].max()
        if (date_max - date_min).days < 30:
            continue
        refund_rate = len(tab.loc[tab["transaction_type"] == "refund"]) / len(tab)
        if refund_rate >= 0.2:
            continue
        res.append(customers.loc[j, "customer_id"])
    return pd.DataFrame(res, columns=["customer_id"]).sort_values(by="customer_id")
