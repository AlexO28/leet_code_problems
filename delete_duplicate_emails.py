# Write a solution to delete all duplicate emails, keeping only one unique email with the smallest id.


import pandas as pd

# Modify Person in place
def delete_duplicate_emails(person: pd.DataFrame) -> None:
    email_stats = person.groupby("email", as_index = False)["id"].aggregate(['count', 'min'])
    email_stats = email_stats[email_stats["count"] > 1]
    del email_stats["count"]
    tab = pd.merge(person, email_stats, how = "left", on = ["email"])
    tab = (tab.loc[(~pd.isnull(tab["min"])) & (tab["min"] != tab["id"]), ["id"]])
    person.drop(tab.index.to_list(), inplace = True)
