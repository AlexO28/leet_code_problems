# Write a solution to find patients who have recovered from COVID - patients who tested positive but later tested negative.
# A patient is considered recovered if they have at least one Positive test followed by at least one Negative test on a later date
# Calculate the recovery time in days as the difference between the first positive test and the first negative test after that positive test
# Only include patients who have both positive and negative test results
# Return the result table ordered by recovery_time in ascending order, then by patient_name in ascending order.
from datetime import datetime
import pandas as pd


def find_covid_recovery_patients(
    patients: pd.DataFrame, covid_tests: pd.DataFrame
) -> pd.DataFrame:
    patients["recovery_time"] = -1
    for j in range(len(patients)):
        tab = covid_tests.loc[
            (covid_tests["patient_id"] == patients.loc[j, "patient_id"])
            & (covid_tests["result"] != "Inconclusive")
        ]
        if len(tab) > 1:
            tab = tab.sort_values(by="test_date").reset_index(drop=True)
            pos_date = None
            neg_date = None
            print(tab)
            for i in range(len(tab)):
                if tab.loc[i, "result"] == "Positive":
                    if pos_date is None:
                        pos_date = datetime.strptime(
                            tab.loc[i, "test_date"], "%Y-%m-%d"
                        ).date()
                else:
                    if pos_date is not None:
                        neg_date = datetime.strptime(
                            tab.loc[i, "test_date"], "%Y-%m-%d"
                        ).date()
                        break
            if (pos_date is not None) and (neg_date is not None):
                patients.loc[j, "recovery_time"] = (neg_date - pos_date).days
    patients = patients.loc[patients["recovery_time"] >= 0]
    return patients.sort_values(by=["recovery_time", "patient_name"])
