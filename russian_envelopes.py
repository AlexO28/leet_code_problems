# You are given a 2D array of integers envelopes where envelopes[i] = [wi, hi] represents the width and the height of an envelope.
# One envelope can fit into another if and only if both the width and height of one envelope are greater than the other envelope's width and height.
# Return the maximum number of envelopes you can Russian doll (i.e., put one inside the other).
from bisect import bisect_left

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        dp = [envelopes[0][1]]
        for width, height in envelopes[1:]:
            if height > dp[-1]:
                dp.append(height)
            else:
                index = bisect_left(dp, height)
                dp[index] = height      
        return len(dp)
