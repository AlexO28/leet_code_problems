# You are given an integer array values where values[i] represents the value of the ith sightseeing spot. Two sightseeing spots i and j have a distance j - i between them.
# The score of a pair (i < j) of sightseeing spots is values[i] + values[j] + i - j: the sum of the values of the sightseeing spots, minus the distance between them.
# Return the maximum score of a pair of sightseeing spots.
from typing import List


class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        if len(values) == 2:
            return sum(values) - 1
        max_score = 0
        max_value_plus_index = values[0]
        for i in range(1, len(values)):
            max_score = max(max_score, values[i] - i + max_value_plus_index)
            max_value_plus_index = max(max_value_plus_index, values[i] + i)
        return max_score
