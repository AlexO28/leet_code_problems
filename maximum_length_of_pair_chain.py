# You are given an array of n pairs pairs where pairs[i] = [lefti, righti] and lefti < righti.
# A pair p2 = [c, d] follows a pair p1 = [a, b] if b < c. A chain of pairs can be formed in this fashion.
# Return the length longest chain which can be formed.
# You do not need to use up all the given intervals. You can select pairs in any order.
import math


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        if len(pairs) == 1:
            return 1
        count = 0
        prevEnd = -math.inf
        for start, end in sorted(pairs, key=lambda x: x[1]):
            if start > prevEnd:
                count += 1
                prevEnd = end
        return count
