# Write a solution to identify emotionally consistent users based on the following requirements:
# For each user, count the total number of reactions they have given.
# Only include users who have reacted to at least 5 different content items.
# A user is considered emotionally consistent if at least 60% of their reactions are of the same type.
# Return the result table ordered by reaction_ratio in descending order and then by user_id in ascending order.
import pandas as pd


def find_emotionally_consistent_users(reactions: pd.DataFrame) -> pd.DataFrame:
    users = reactions[["user_id"]].drop_duplicates().reset_index(drop=True)
    users["dominant_reaction"] = ""
    users["reaction_ratio"] = -1
    for j in range(len(users)):
        tab = reactions.loc[(reactions["user_id"] == users.loc[j, "user_id"])]
        if len(tab) < 5:
            continue
        tab_agg = tab[["reaction"]].value_counts(normalize=True).reset_index()
        reaction = tab_agg.loc[0, "reaction"]
        reaction_ratio = tab_agg.loc[0, "proportion"]
        if reaction_ratio < 0.6:
            continue
        users.loc[j, "dominant_reaction"] = reaction
        users.loc[j, "reaction_ratio"] = round(reaction_ratio + 0.0001, 2)
    return users.loc[users["reaction_ratio"] > 0].sort_values(
        by=["reaction_ratio", "user_id"], ascending=[False, True]
    )
