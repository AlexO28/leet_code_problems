# Write a solution to find the nth highest salary from the Employee table. If there is no nth highest salary, return null.

import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    employee.sort_values("salary", inplace = True, ascending = False)
    employee = employee["salary"]
    employee.drop_duplicates(inplace = True)
    employee = pd.DataFrame(employee, columns = ["salary"])
    name = "getNthHighestSalary(" + str(N) + ")"
    if len(employee) < N:
        return pd.DataFrame([None], columns = [name])
    return pd.DataFrame([employee["salary"].values.tolist()[N-1]], columns = [name])
