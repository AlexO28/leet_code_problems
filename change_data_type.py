# Write a solution to correct the errors:
# The grade column is stored as floats, convert it to integers.
import pandas as pd

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    students["grade"] = students["grade"].astype(int)
    return students 
