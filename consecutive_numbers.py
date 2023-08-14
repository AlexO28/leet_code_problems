# Find all numbers that appear at least three times consecutively.
# Return the result table in any order.

import pandas as pd

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    vals = []
    trivial_df = pd.DataFrame([], columns = ["ConsecutiveNums"])
    if len(logs) == 0:
        return trivial_df
    vals = []
    prev_val = None
    multiplicity = 1
    for i in range(len(logs)):
        val = logs.at[i, "num"]
        if val == prev_val:
            multiplicity += 1
        else:
            if multiplicity >= 3:
                if prev_val not in vals:
                    vals.append(prev_val)
            multiplicity = 1
            prev_val = val
    if multiplicity >= 3:
        if prev_val not in vals:
            vals.append(prev_val)
    if len(vals) == 0:
        return trivial_df
    return pd.DataFrame(vals, columns = ["ConsecutiveNums"])
