# Given a data stream input of non-negative integers a1, a2, ..., an, summarize the numbers seen so far as a list of disjoint intervals.
# Implement the SummaryRanges class:
# SummaryRanges() Initializes the object with an empty stream.
# void addNum(int value) Adds the integer value to the stream.
# int[][] getIntervals() Returns a summary of the integers in the stream currently as a list of disjoint intervals [starti, endi]. The answer should be sorted by starti.
import sortedcontainers

class SummaryRanges:
    def __init__(self):
        self.keys = sortedcontainers.SortedDict()
        
    def addNum(self, value: int) -> None:
        if value not in self.keys:
            lower = self.lowerKey(value)
            upper = self.upperKey(value)
            if (lower is not None) and (upper is not None) and\
                (self.keys[lower][1] + 1 == value) and (upper - 1 == value):
                self.keys[lower][1] = self.keys[upper][1]
                del self.keys[upper]
            elif (lower is not None) and (self.keys[lower][1] >= value - 1):
                self.keys[lower][1] = max(value, self.keys[lower][1])
            elif (upper is not None) and (upper == value + 1):
                self.keys[value] = [value, self.keys[upper][1]]
                del self.keys[upper]
            else:
                self.keys[value] = [value, value]
        
    def getIntervals(self) -> List[List[int]]:
        return list(self.keys.values())

    def lowerKey(self, value):
        left = self.keys.bisect_left(value)
        if left != 0:
            return self.keys.keys()[left-1]
    
    def upperKey(self, value):
        right = self.keys.bisect_right(value)
        if right != len(self.keys):
            return self.keys.keys()[right]
        
# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()
