# Write a program to count the number of days between two dates.
# The two dates are given as strings, their format is YYYY-MM-DD as shown in the examples.
import datetime


class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        return abs(
            (
                datetime.datetime.strptime(date1, "%Y-%m-%d")
                - datetime.datetime.strptime(date2, "%Y-%m-%d")
            ).days
        )
