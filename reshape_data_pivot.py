# Write a solution to pivot the data so that each row represents temperatures for a specific month, and each city is a separate column.
import pandas as pd


def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    weather = weather.pivot(columns=["city"], index=["month"])
    weather.columns = [col[-1] for col in weather.columns]
    return weather
