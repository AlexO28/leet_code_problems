# A subscription service wants to analyze user behavior patterns. The company offers a 7-day free trial, after which users can subscribe to a paid plan or cancel. Write a solution to:
# Find users who converted from free trial to paid subscription
# Calculate each user's average daily activity duration during their free trial period (rounded to 2 decimal places)
# Calculate each user's average daily activity duration during their paid subscription period (rounded to 2 decimal places)
# Return the result table ordered by user_id in ascending order.
import pandas as pd


def analyze_subscription_conversion(user_activity: pd.DataFrame) -> pd.DataFrame:
    users = set(user_activity["user_id"].values.tolist())
    res = []
    for user in users:
        tab = user_activity.loc[
            (user_activity["user_id"] == user)
            & (user_activity["activity_type"] != "cancelled")
        ].sort_values(by="activity_date")
        if (tab["activity_type"].values.tolist()[0] == "free_trial") and (
            tab["activity_type"].values.tolist()[-1] == "paid"
        ):
            tabred = (
                tab.loc[tab["activity_type"] == "free_trial"]
                .groupby("activity_date")["activity_duration"]
                .sum()
                .reset_index()
            )
            num1 = round(
                ((tabred["activity_duration"].sum() + 0.0000001) / len(tabred)), 2
            )
            tabred = (
                tab.loc[tab["activity_type"] == "paid"]
                .groupby("activity_date")["activity_duration"]
                .sum()
                .reset_index()
            )
            num2 = round(
                ((tabred["activity_duration"].sum() + 0.0000001) / len(tabred)), 2
            )
            res.append([user, num1, num2])
    return pd.DataFrame(
        res, columns=["user_id", "trial_avg_duration", "paid_avg_duration"]
    )
