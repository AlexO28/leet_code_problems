# Given a list of 24-hour clock time points in "HH:MM" format, return the minimum minutes difference between any two time-points in the list.
import datetime

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        if len(timePoints) > 1440:
            return 0
        timePoints = [datetime.datetime.strptime(point, '%H:%M') for point in timePoints]
        diff = 1441
        for i in range(len(timePoints)-1):
            for j in range(i+1, len(timePoints)):
                diff = min(diff, self.comparePoints(timePoints[i], timePoints[j]))
        return int(diff)

    def comparePoints(self, point1, point2):
        diff = abs((point1 - point2).total_seconds()/60)
        return min(diff, 1440-diff)
