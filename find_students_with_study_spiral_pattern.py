# Write a solution to find students who follow the Study Spiral Pattern - students who consistently study multiple subjects in a rotating cycle.
# A Study Spiral Pattern means a student studies at least 3 different subjects in a repeating sequence
# The pattern must repeat for at least 2 complete cycles (minimum 6 study sessions)
# Sessions must be consecutive dates with no gaps longer than 2 days between sessions
# Calculate the cycle length (number of different subjects in the pattern)
# Calculate the total study hours across all sessions in the pattern
# Only include students with cycle length of at least 3 subjects
# Return the result table ordered by cycle length in descending order, then by total study hours in descending order.
import pandas as pd
from datetime import datetime


def find_study_spiral_pattern(
    students: pd.DataFrame, study_sessions: pd.DataFrame
) -> pd.DataFrame:
    students["cycle_length"] = 0
    students["total_study_hours"] = 0
    study_sessions["session_date"] = study_sessions["session_date"].apply(
        lambda x: datetime.strptime(x, "%Y-%m-%d")
    )
    for j in range(len(students)):
        tab = study_sessions.loc[
            study_sessions["student_id"] == students.loc[j, "student_id"]
        ]
        if len(tab) > 5:
            tab = tab.sort_values(by=["session_date"]).reset_index(drop=True)
            date_cur = tab.loc[0, "session_date"]
            fail = False
            for i in range(1, len(tab)):
                if (tab.loc[i, "session_date"] - date_cur).days > 2:
                    fail = True
                    break
                else:
                    date_cur = tab.loc[i, "session_date"]
            if fail:
                continue
            pattern_set = set(tab["subject"].drop_duplicates())
            if len(pattern_set) < 3:
                continue
            main_part, remainder = divmod(len(tab), len(pattern_set))
            if main_part < 2:
                continue
            pattern = list(tab["subject"][: len(pattern_set)].values)
            full = list(tab["subject"].values)
            i = 0
            faul = False
            for k in range(len(full)):
                if pattern[i] != full[k]:
                    fail = True
                    continue
                else:
                    k += 1
                    if k == len(pattern):
                        k = 0
            students.loc[j, "cycle_length"] = len(pattern_set)
            students.loc[j, "total_study_hours"] = tab["hours_studied"].sum()
    return students.loc[students["cycle_length"] > 2].sort_values(
        by=["cycle_length", "total_study_hours"], ascending=False
    )
