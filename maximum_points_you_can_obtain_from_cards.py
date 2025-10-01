# There are several cards arranged in a row, and each card has an associated number of points. The points are given in the integer array cardPoints.
# In one step, you can take one card from the beginning or from the end of the row. You have to take exactly k cards.
# Your score is the sum of the points of the cards you have taken.
# Given the integer array cardPoints and the integer k, return the maximum score you can obtain.
from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if len(cardPoints) == k:
            return sum(cardPoints)
        total_points = sum(cardPoints)
        delta = len(cardPoints) - k
        cur_sum = sum(cardPoints[:delta])
        res = total_points - cur_sum
        for j in range(1, k + 1):
            cur_sum += cardPoints[delta - 1 + j] - cardPoints[j - 1]
            res = max(res, total_points - cur_sum)
        return res
