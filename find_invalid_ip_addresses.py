# Write a solution to find invalid IP addresses. An IPv4 address is invalid if it meets any of these conditions:
# Contains numbers greater than 255 in any octet
# Has leading zeros in any octet (like 01.02.03.04)
# Has less or more than 4 octets
# Return the result table ordered by invalid_count, ip in descending order respectively. 
# The result format is in the following example.
import pandas as pd


def find_invalid_ips(logs: pd.DataFrame) -> pd.DataFrame:
    logs["valid"] = logs["ip"].apply(lambda x: is_valid(x))
    logs = (
        logs.loc[logs["valid"] == False]
        .groupby("ip")["log_id"]
        .count()
        .reset_index()
        .rename(columns={"log_id": "invalid_count"})
    )
    return logs.sort_values(by=["invalid_count", "ip"], ascending=False)


def is_valid(text):
    words = text.split(".")
    if len(words) != 4:
        return False
    for word in words:
        try:
            num = int(word)
        except:
            return False
        if num > 255:
            return False
        if len(str(num)) != len(word):
            return False
    return True
