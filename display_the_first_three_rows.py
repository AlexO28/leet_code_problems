# Write a solution to display the first 3 rows of this DataFrame.
import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.head(3)
