# Alice and Bob are traveling to Rome for separate business meetings.
# You are given 4 strings arriveAlice, leaveAlice, arriveBob, and leaveBob. Alice will be in the city from the dates arriveAlice to leaveAlice (inclusive), while Bob will be in the city from the dates arriveBob to leaveBob (inclusive). Each will be a 5-character string in the format "MM-DD", corresponding to the month and day of the date.
# Return the total number of days that Alice and Bob are in Rome together.
# You can assume that all dates occur in the same calendar year, which is not a leap year. Note that the number of days per month can be represented as: [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31].
from datetime import date


class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        arriveAlice = self._toDate(arriveAlice)
        leaveAlice = self._toDate(leaveAlice)
        arriveBob = self._toDate(arriveBob)
        leaveBob = self._toDate(leaveBob)
        arrival = max(arriveAlice, arriveBob)
        departure = min(leaveAlice, leaveBob)
        days = (departure - arrival).days
        if days < 0:
            return 0
        else:
            return days + 1

    def _toDate(self, dateStr):
        return date.fromisoformat("2026-" + dateStr.replace(".", "-"))
