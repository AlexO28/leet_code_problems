# Given a positive integer n, find and return the longest distance between any two adjacent 1's in the binary representation of n. If there are no two adjacent 1's, return 0.
# Two 1's are adjacent if there are only 0's separating them (possibly no 0's). The distance between two 1's is the absolute difference between their bit positions. For example, the two 1's in "1001" have a distance of 3.
class Solution:
    def binaryGap(self, n: int) -> int:
        n = str(bin(n))[2:]
        if len(n) == 1:
            return 0
        first_ind = -1
        res = 0
        for i in range(len(n)):
            if n[i] == "1":
                if first_ind >= 0:
                    res = max(res, i - first_ind)
                first_ind = i
        return res
