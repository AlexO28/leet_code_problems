# A chef has collected data on the satisfaction level of his n dishes. Chef can cook any dish in 1 unit of time.
# Like-time coefficient of a dish is defined as the time taken to cook that dish including previous dishes multiplied by its satisfaction level i.e. time[i] * satisfaction[i].
# Return the maximum sum of like-time coefficient that the chef can obtain after preparing some amount of dishes.
# Dishes can be prepared in any order and the chef can discard some dishes to get this maximum value.
from typing import List


class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse=True)
        max_like_time_coefficient = 0
        cumulative_sum = 0
        for dish_satisfaction in satisfaction:
            cumulative_sum += dish_satisfaction
            if cumulative_sum <= 0:
                break
            max_like_time_coefficient += cumulative_sum
        return max_like_time_coefficient
