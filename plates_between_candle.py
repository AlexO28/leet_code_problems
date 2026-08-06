# There is a long table with a line of plates and candles arranged on top of it. You are given a 0-indexed string s consisting of characters '*' and '|' only, where a '*' represents a plate and a '|' represents a candle.
# You are also given a 0-indexed 2D integer array queries where queries[i] = [lefti, righti] denotes the substring s[lefti...righti] (inclusive). For each query, you need to find the number of plates between candles that are in the substring. A plate is considered between candles if there is at least one candle to its left and at least one candle to its right in the substring.
# For example, s = "||**||**|*", and a query [3, 8] denotes the substring "*||**|". The number of plates between candles in this substring is 2, as each of the two plates has at least one candle in the substring to its left and right.
# Return an integer array answer where answer[i] is the answer to the ith query.
import bisect
from typing import List


class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        candle_indices = []
        prefix_sums = []
        number_of_plates = 0
        for j in range(len(s)):
            if s[j] == "|":
                candle_indices.append(j)
            else:
                number_of_plates += 1
            prefix_sums.append(number_of_plates)
        res = []
        for left, right in queries:
            left_ind = bisect.bisect_left(candle_indices, left)
            if left_ind == len(candle_indices):
                res.append(0)
                continue
            left_ind = candle_indices[left_ind]
            right_ind = bisect.bisect_right(candle_indices, right) - 1
            if (right_ind == -1):
                res.append(0)
                continue
            right_ind = candle_indices[right_ind]
            if (left_ind >= right_ind):
                res.append(0)
                continue
            res.append(
                prefix_sums[right_ind] - prefix_sums[left_ind]
            )
        return res
