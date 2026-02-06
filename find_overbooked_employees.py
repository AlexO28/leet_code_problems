# Write a solution to find employees who are meeting-heavy - employees who spend more than 50% of their working time in meetings during any given week.
# Assume a standard work week is 40 hours
# Calculate total meeting hours per employee per week (Monday to Sunday)
# An employee is meeting-heavy if their weekly meeting hours > 20 hours (50% of 40 hours)
# Count how many weeks each employee was meeting-heavy
# Only include employees who were meeting-heavy for at least 2 weeks
# Return the result table ordered by the number of meeting-heavy weeks in descending order, then by employee name in ascending order.
# The result format is in the following example.
import pandas as pd


def find_overbooked_employees(
    employees: pd.DataFrame, meetings: pd.DataFrame
) -> pd.DataFrame:
    meetings["meeting_date"] = pd.to_datetime(meetings["meeting_date"])
    meetings["year"] = meetings["meeting_date"].dt.isocalendar().year
    meetings["week"] = meetings["meeting_date"].dt.isocalendar().week

    week_meeting_hours = (
        meetings.groupby(["employee_id", "year", "week"], as_index=False)[
            "duration_hours"
        ]
        .sum()
        .rename(columns={"duration_hours": "hours"})
    )

    intensive_weeks = week_meeting_hours[week_meeting_hours["hours"] >= 20]

    intensive_count = (
        intensive_weeks.groupby("employee_id")
        .size()
        .reset_index(name="meeting_heavy_weeks")
    )

    result = intensive_count.merge(employees, on="employee_id")

    result = result[result["meeting_heavy_weeks"] >= 2]

    result = result.sort_values(
        ["meeting_heavy_weeks", "employee_name"], ascending=[False, True]
    )

    return result[
        ["employee_id", "employee_name", "department", "meeting_heavy_weeks"]
    ].reset_index(drop=True)
