# Write a solution to find the second highest salary from the Employee table. If there is no second highest salary, return null (return None in Pandas).

import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    employee.sort_values("salary", inplace = True, ascending = False)
    employee = employee["salary"]
    employee.drop_duplicates(inplace = True)
    employee = pd.DataFrame(employee, columns = ["salary"])
    if len(employee) < 2:
        return pd.DataFrame([None], columns = ["SecondHighestSalary"])
    return pd.DataFrame([employee["salary"].values.tolist()[1]], columns = ["SecondHighestSalary"])
    
