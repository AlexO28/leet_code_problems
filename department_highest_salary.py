# Write a solution to find employees who have the highest salary in each of the departments.


import pandas as pd


def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    department.rename(columns = {"id": "departmentId", "name": "departmentName"}, inplace = True)
    dep_with_salary = pd.merge(employee, department,
                               left_on = ["departmentId"], right_on = ["departmentId"],
                               how = "inner")
    dep_with_salary_max = dep_with_salary.groupby("departmentId", as_index = False)["salary"].max()
    dep_with_salary_max = pd.merge(dep_with_salary, dep_with_salary_max,
                                   how = "inner",
                                   on = ["departmentId", "salary"])
    res = dep_with_salary_max[["departmentId", "id", "name", "salary"]]
    res = pd.merge(res, department, how = "inner",
                   on = ["departmentId"])
    res = res[["departmentName", "name", "salary"]]
    res.rename(columns = {"departmentName": "Department",
                          "name": "Employee",
                          "salary": "Salary"}, inplace = True)
    return res
