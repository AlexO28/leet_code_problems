import numpy as np


class MedianFinder:

    def __init__(self):
        self.arr = [] 

    def addNum(self, num: int) -> None:
        if len(self.arr) == 0:
            self.arr.append(num)
        else:
            self.addNumToListSubset(num, 0, len(self.arr)-1)

    def addNumToListSubset(self, num, i, j):
        if i == j:
            if num <= self.arr[i]:
                self.arr.insert(i, num)
            else:
                self.arr.insert(i+1, num)
        elif j - i == 1:
            if num <= self.arr[i]:
                self.arr.insert(i, num)
            elif num <= self.arr[j]:
                self.arr.insert(j, num)
            else:
                self.arr.insert(j+1, num)
        else:
            if num <= self.arr[i]:
                self.arr.insert(i, num)
            elif num >= self.arr[j]:
                self.arr.insert(j+1, num)
            else:
                mid_index = int((i + j)/2)
                if num < self.arr[mid_index]:
                    self.addNumToListSubset(num, i, mid_index)
                else:
                    self.addNumToListSubset(num, mid_index, j)

    def findMedian(self) -> float:
        if len(self.arr) % 2 == 0:
            mid_index = int(len(self.arr)/2)
            return (self.arr[mid_index-1] + self.arr[mid_index])/2
        else:
            return self.arr[int(np.floor(len(self.arr)/2))]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
