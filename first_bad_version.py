# You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:

    def firstBadVersion(self, n: int) -> int:
        return self.findBadVersion(1, n)

    def findBadVersion(self, start, end):
        if end == start:
            return start
        elif end == start + 1:
            if isBadVersion(start):
                return start
            else:
                return end
        middle = int((start + end)/2)
        if isBadVersion(middle):
            return self.findBadVersion(start, middle)
        else:
            return self.findBadVersion(middle, end)
