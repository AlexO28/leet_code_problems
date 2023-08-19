# Write a solution to report all the duplicate emails. 

import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    person_2 = person.copy()
    person_2.rename(columns = {"id": "id_2"}, inplace = True)
    tab = pd.merge(person, person_2, on=["email"], how="inner")
    tab = tab[tab["id"] != tab["id_2"]]
    tab = tab[["email"]].drop_duplicates()
    tab.rename(columns = {"email": "Email"}, inplace = True)
    return tab
