# Write a solution to find all the valid email addresses. A valid email address meets the following criteria:
# It contains exactly one @ symbol.
# It ends with .com.
# The part before the @ symbol contains only alphanumeric characters and underscores.
# The part after the @ symbol and before .com contains a domain name that contains only letters.
# Return the result table ordered by user_id in ascending order.
import pandas as pd


def find_valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    users["valid"] = users["email"].apply(lambda x: is_valid(x))
    return users.loc[users["valid"] == True][["user_id", "email"]].sort_values(
        by="user_id"
    )


def is_valid(text):
    before = []
    after = []
    text = list(text)
    found = False
    first_part = []
    second_part = []
    for elem in text:
        if elem == "@":
            if not found:
                found = True
            else:
                return False
        else:
            if not found:
                first_part.append(elem)
            else:
                second_part.append(elem)
    first_part = "".join(first_part)
    second_part = "".join(second_part)
    if len(second_part) < 4:
        return False
    if second_part[(-4):] != ".com":
        return False
    return first_part.replace("_", "").isalnum() and second_part[:(-4)].isalpha()
