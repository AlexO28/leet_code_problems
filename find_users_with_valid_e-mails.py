# Write a solution to find the users who have valid emails.

import re
import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    inds = []
    for j, row in users.iterrows():
        email = row["mail"]
        if "@" in email:
            temp = email.split('@')
            if len(temp) == 2:
                if temp[1] == "leetcode.com":
                    email = temp[0].lower()
                    if email[0] in 'abcdefghijklmnopqrstuvwxyz':
                        if re.sub('[^0-9a-z_\.-]+', '', email) == email:
                            inds.append(j)
    return users.loc[inds, :]
