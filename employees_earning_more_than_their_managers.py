# Write a solution to find the employees who earn more than their managers.

import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    managers = employee.copy()
    del managers["managerId"], managers["name"]
    managers.rename(columns = {"id": "managerId", "salary": "managerSalary"}, inplace = True)
    tab = pd.merge(employee, managers, how = "left", on = ["managerId"])
    tab = tab[tab["salary"] > tab["managerSalary"]]
    tab.rename(columns = {"name": "Employee"}, inplace = True)
    return tab[["Employee"]]
