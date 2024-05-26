# You are implementing a program to use as your calendar. We can add a new event if adding the event will not cause a triple booking.
# A triple booking happens when three events have some non-empty intersection (i.e., some moment is common to all the three events.).
# The event can be represented as a pair of integers start and end that represents a booking on the half-open interval [start, end), the range of real numbers x such that start <= x < end.
# Implement the MyCalendarTwo class:
# MyCalendarTwo() Initializes the calendar object.
# boolean book(int start, int end) Returns true if the event can be added to the calendar successfully without causing a triple booking. Otherwise, return false and do not add the event to the calendar.
class MyCalendarTwo:

    def __init__(self):
        self.intervals = []
        self.conflicts = []
        

    def book(self, start: int, end: int) -> bool:
        if len(self.intervals) == 0:
            self.intervals.append([start, end])
            return True
        if len(self.conflicts) > 0:
            for conflict in self.conflicts:
                if not ((end <= conflict[0]) or (start >= conflict[1])):
                    return False
        for interval in self.intervals:
            if not ((end <= interval[0]) or (start >= interval[1])):
                self.conflicts.append([max(start, interval[0]), min(end, interval[1])])
        self.intervals.append([start, end])
        return True
