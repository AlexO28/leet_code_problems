# Write a solution to identify behaviorally stable users based on the following definition:
# A user is considered behaviorally stable if there exists a sequence of at least 5 consecutive days such that:
# The user performed exactly one action per day during that period.
# The action is the same on all those consecutive days.
# If a user has multiple qualifying sequences, only consider the sequence with the maximum length.
# Return the result table ordered by streak_length in descending order, then by user_id in ascending order.
import pandas as pd
from datetime import datetime


def find_behaviorally_stable_users(activity: pd.DataFrame) -> pd.DataFrame:
    activity["action_date"] = activity["action_date"].apply(
        lambda x: datetime.strptime(x, "%Y-%m-%d")
    )
    users = activity[["user_id"]].drop_duplicates().reset_index(drop=True)
    users["action"] = ""
    users["streak_length"] = 0
    users["start_date"] = datetime.strptime("1970-01-01", "%Y-%m-%d")
    users["end_date"] = datetime.strptime("1970-01-01", "%Y-%m-%d")
    for j in range(len(users)):
        tab = (
            activity.loc[(activity["user_id"] == users.loc[j, "user_id"])]
            .sort_values(by="action_date")
            .reset_index(drop=True)
        )
        if len(tab) < 5:
            continue
        emotion = tab.loc[0, "action"]
        start_date = tab.loc[0, "action_date"]
        strike_length = 1
        max_strike = 1
        max_emotion = emotion
        max_start_date = start_date
        for i in range(1, len(tab)):
            if (tab.loc[i, "action"] == emotion) and (
                (tab.loc[i, "action_date"] - tab.loc[i - 1, "action_date"]).days == 1
            ):
                strike_length += 1
            else:
                if strike_length > max_strike:
                    max_strike = strike_length
                    max_emotion = emotion
                    max_start_date = start_date
                    max_end_date = tab.loc[(i - 1), "action_date"]
                strike_length = 1
                emotion = tab.loc[i, "action"]
                start_date = tab.loc[i, "action_date"]
        if strike_length > max_strike:
            max_strike = strike_length
            max_emotion = emotion
            max_start_date = start_date
            max_end_date = tab.loc[len(tab) - 1, "action_date"]
        if max_strike < 5:
            continue
        users.loc[j, "action"] = max_emotion
        users.loc[j, "streak_length"] = max_strike
        users.loc[j, "start_date"] = max_start_date
        users.loc[j, "end_date"] = max_end_date
    return users.loc[users["streak_length"] > 0].sort_values(
        by=["streak_length", "user_id"], ascending=[False, True]
    )
