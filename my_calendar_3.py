# A k-booking happens when k events have some non-empty intersection (i.e., there is some time that is common to all k events.)
# You are given some events [startTime, endTime), after each given event, return an integer k representing the maximum k-booking between all the previous events.
# Implement the MyCalendarThree class:
# MyCalendarThree() Initializes the object.
# int book(int startTime, int endTime) Returns an integer k representing the largest integer such that there exists a k-booking in the calendar.
from sortedcontainers import SortedDict


class MyCalendarThree:

    def __init__(self):
        self.timeline = SortedDict()

    def book(self, startTime: int, endTime: int) -> int:
        self.timeline[startTime] = self.timeline.get(startTime, 0) + 1
        self.timeline[endTime] = self.timeline.get(endTime, 0) - 1
        return max(accumulate(list(self.timeline.values())))
