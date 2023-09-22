# Write a solution to find the patient_id, patient_name, and conditions of the patients who have Type I Diabetes. Type I Diabetes always starts with DIAB1 prefix.

import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    inds = []
    for i, row in patients.iterrows():
        condition = row["conditions"]
        condition_list = condition.split(" ")
        for elem in condition_list:
            if len(elem) >= 5:
                if elem[:5] == "DIAB1":
                    inds.append(i)
                    break
    return patients.loc[inds, :]
 
