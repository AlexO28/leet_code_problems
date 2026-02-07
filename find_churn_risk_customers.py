# Write a solution to Find Churn Risk Customers - users who show warning signs before churning. A user is considered churn risk customer if they meet ALL the following criteria:
# Currently have an active subscription (their last event is not cancel).
# Have performed at least one downgrade in their subscription history.
# Their current plan revenue is less than 50% of their historical maximum plan revenue.
# Have been a subscriber for at least 60 days.
# Return the result table ordered by days_as_subscriber in descending order, then by user_id in ascending order.
import pandas as pd
from datetime import datetime


def find_churn_risk_customers(subscription_events: pd.DataFrame) -> pd.DataFrame:
    subscription_events["event_date"] = subscription_events["event_date"].apply(
        lambda x: datetime.strptime(x, "%Y-%m-%d")
    )
    users = subscription_events[["user_id"]].drop_duplicates().reset_index(drop=True)
    users["current_plan"] = ""
    users["current_monthly_amount"] = -1
    users["max_historical_amount"] = -1
    users["days_as_subscriber"] = -1
    for j in range(len(users)):
        tab = (
            subscription_events.loc[
                subscription_events["user_id"] == users.loc[j, "user_id"]
            ]
            .sort_values(by="event_date")
            .reset_index(drop=True)
        )
        if tab.loc[len(tab) - 1, "event_type"] == "cancel":
            continue
        if "downgrade" not in set(tab["event_type"].drop_duplicates()):
            continue
        current_montly_amount = tab.loc[len(tab) - 1, "monthly_amount"]
        max_historical_amount = tab["monthly_amount"].max()
        if current_montly_amount >= max_historical_amount / 2:
            continue
        date_start = tab.loc[0, "event_date"]
        date_end = tab.loc[len(tab) - 1, "event_date"]
        date_diff = (date_end - date_start).days
        if date_diff < 60:
            continue
        users.loc[j, "current_plan"] = tab.loc[len(tab) - 1, "plan_name"]
        users.loc[j, "current_monthly_amount"] = current_montly_amount
        users.loc[j, "max_historical_amount"] = max_historical_amount
        users.loc[j, "days_as_subscriber"] = date_diff
    return users.loc[users["days_as_subscriber"] > 0].sort_values(
        by=["days_as_subscriber", "user_id"], ascending=[False, True]
    )
