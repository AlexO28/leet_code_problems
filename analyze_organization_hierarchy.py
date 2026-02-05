# Write a solution to analyze the organizational hierarchy and answer the following:
# Hierarchy Levels: For each employee, determine their level in the organization (CEO is level 1, employees reporting directly to the CEO are level 2, and so on).
# Team Size: For each employee who is a manager, count the total number of employees under them (direct and indirect reports).
# Salary Budget: For each manager, calculate the total salary budget they control (sum of salaries of all employees under them, including indirect reports, plus their own salary).
# Return the result table ordered by the result ordered by level in ascending order, then by budget in descending order, and finally by employee_name in ascending order.
import pandas as pd


def analyze_organization_hierarchy(employees: pd.DataFrame) -> pd.DataFrame:
    employees["level"] = None
    ceo_id = employees.loc[employees["manager_id"].isna(), "employee_id"].values[0]
    employees.loc[employees["employee_id"] == ceo_id, "level"] = 1
    compute_levels(employees, 1)
    team_size = {eid: 0 for eid in employees["employee_id"]}
    budget = {
        eid: salary
        for eid, salary in zip(employees["employee_id"], employees["salary"])
    }
    for eid in sorted(employees["employee_id"], reverse=True):
        manager_id = employees.loc[
            employees["employee_id"] == eid, "manager_id"
        ].values[0]
        if pd.notna(manager_id):
            team_size[manager_id] += team_size[eid] + 1
            budget[manager_id] += budget[eid]
    employees["team_size"] = employees["employee_id"].map(team_size)
    employees["budget"] = employees["employee_id"].map(budget)
    employees = employees.sort_values(
        by=["level", "budget", "employee_name"], ascending=[True, False, True]
    )
    return employees[["employee_id", "employee_name", "level", "team_size", "budget"]]


def compute_levels(emp_df, level):
    next_level_ids = emp_df[emp_df["level"] == level]["employee_id"].tolist()
    if next_level_ids:
        emp_df.loc[emp_df["manager_id"].isin(next_level_ids), "level"] = level + 1
        compute_levels(emp_df, level + 1)
