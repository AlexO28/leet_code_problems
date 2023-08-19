# Write a solution to report the first name, last name, city, and state of each person in the Person table. If the address of a personId is not present in the Address table, report null instead.

import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    tab = pd.merge(person, address, how = "left", on = ["personId"])
    return tab[["firstName", "lastName", "city", "state"]]
