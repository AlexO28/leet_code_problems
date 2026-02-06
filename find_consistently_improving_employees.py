# Write a solution to find employees who have consistently improved their performance over their last three reviews.
# An employee must have at least 3 review to be considered
# The employee's last 3 reviews must show strictly increasing ratings (each review better than the previous)
# Use the most recent 3 reviews based on review_date for each employee
# Calculate the improvement score as the difference between the latest rating and the earliest rating among the last 3 reviews
# Return the result table ordered by improvement score in descending order, then by name in ascending order.
import pandas as pd


def find_consistently_improving_employees(
    employees: pd.DataFrame, performance_reviews: pd.DataFrame
) -> pd.DataFrame:
    employees["improvement_score"] = 0
    for j in range(len(employees)):
        tab = performance_reviews.loc[
            performance_reviews["employee_id"] == employees.loc[j, "employee_id"]
        ]
        if len(tab) >= 3:
            tab = tab.sort_values("review_date", ascending=False).reset_index(drop=True)
            if (tab.loc[0, "rating"] > tab.loc[1, "rating"]) and (
                tab.loc[1, "rating"] > tab.loc[2, "rating"]
            ):
                employees.loc[j, "improvement_score"] = (
                    tab.loc[0, "rating"] - tab.loc[2, "rating"]
                )
    return employees.loc[employees["improvement_score"] > 0].sort_values(
        by=["improvement_score", "name"], ascending=[False, True]
    )
