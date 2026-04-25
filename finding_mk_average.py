# You are given two integers, m and k, and a stream of integers. You are tasked to implement a data structure that calculates the MKAverage for the stream.
# The MKAverage can be calculated using these steps:
# If the number of the elements in the stream is less than m you should consider the MKAverage to be -1. Otherwise, copy the last m elements of the stream to a separate container.
# Remove the smallest k elements and the largest k elements from the container.
# Calculate the average value for the rest of the elements rounded down to the nearest integer.
# Implement the MKAverage class:
# MKAverage(int m, int k) Initializes the MKAverage object with an empty stream and the two integers m and k.
# void addElement(int num) Inserts a new element num into the stream.
# int calculateMKAverage() Calculates and returns the MKAverage for the current stream rounded down to the nearest integer.
from collections import deque
from sortedcontainers import SortedList


class MKAverage:
    def __init__(self, m: int, k: int):
        self.m = m
        self.k = k
        self.sl = SortedList()
        self.q = deque()
        self.s = 0

    def addElement(self, num: int) -> None:
        self.q.append(num)
        if len(self.q) == self.m:
            self.sl = SortedList(self.q)
            self.s = sum(self.sl[self.k : -self.k])
        elif len(self.q) > self.m:
            i = self.sl.bisect_left(num)
            if i < self.k:
                self.s += self.sl[self.k - 1]
            elif self.k <= i <= self.m - self.k:
                self.s += num
            else:
                self.s += self.sl[self.m - self.k]
            self.sl.add(num)
            x = self.q.popleft()
            i = self.sl.bisect_left(x)
            if i < self.k:
                self.s -= self.sl[self.k]
            elif self.k <= i <= self.m - self.k:
                self.s -= x
            else:
                self.s -= self.sl[self.m - self.k]
            self.sl.remove(x)

    def calculateMKAverage(self) -> int:
        if len(self.sl) < self.m:
            return -1
        else:
            return self.s // (self.m - self.k * 2)
