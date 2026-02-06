# Write a solution to find drivers whose fuel efficiency has improved by comparing their average fuel efficiency in the first half of the year with the second half of the year.
# Calculate fuel efficiency as distance_km / fuel_consumed for each trip
# First half: January to June, Second half: July to December
# Only include drivers who have trips in both halves of the year
# Calculate the efficiency improvement as (second_half_avg - first_half_avg)
# Round all results to 2 decimal places
# Return the result table ordered by efficiency improvement in descending order, then by driver name in ascending order.
from datetime import datetime
import pandas as pd


def find_improved_efficiency_drivers(
    drivers: pd.DataFrame, trips: pd.DataFrame
) -> pd.DataFrame:
    trips["month"] = trips["trip_date"].apply(
        lambda x: datetime.strptime(x, "%Y-%m-%d").date().month
    )
    trips["efficiency"] = trips["distance_km"] / trips["fuel_consumed"]
    trips1 = trips.loc[trips.month <= 6]
    trips2 = trips.loc[trips.month >= 7]
    drivers["first_half_avg"] = -1
    drivers["second_half_avg"] = -1
    drivers["efficiency_improvement"] = -1
    for j in range(len(drivers)):
        tab1 = trips1.loc[trips1["driver_id"] == drivers.loc[j, "driver_id"]]
        tab2 = trips2.loc[trips2["driver_id"] == drivers.loc[j, "driver_id"]]
        if (len(tab1) > 0) and (len(tab2) > 0):
            drivers.loc[j, "first_half_avg"] = round(
                tab1["efficiency"].mean() + 0.0001, 2
            )
            drivers.loc[j, "second_half_avg"] = round(
                tab2["efficiency"].mean() + 0.0001, 2
            )
            drivers.loc[j, "efficiency_improvement"] = round(
                tab2["efficiency"].mean() - tab1["efficiency"].mean() + 0.0001, 2
            )
    return drivers.loc[drivers["efficiency_improvement"] > 0].sort_values(
        by=["efficiency_improvement", "driver_name"], ascending=[False, True]
    )
