# You have n flower seeds. Every seed must be planted first before it can begin to grow, then bloom. Planting a seed takes time and so does the growth of a seed. You are given two 0-indexed integer arrays plantTime and growTime, of length n each:
# plantTime[i] is the number of full days it takes you to plant the ith seed. Every day, you can work on planting exactly one seed. You do not have to work on planting the same seed on consecutive days, but the planting of a seed is not complete until you have worked plantTime[i] days on planting it in total.
# growTime[i] is the number of full days it takes the ith seed to grow after being completely planted. After the last day of its growth, the flower blooms and stays bloomed forever.
# From the beginning of day 0, you can plant the seeds in any order.
# Return the earliest possible day where all seeds are blooming.
from typing import List


class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        sorted_indices = sorted(
            range(len(growTime)), key=lambda i: growTime[i], reverse=True
        )
        growTime = [growTime[i] for i in sorted_indices]
        plantTime = [plantTime[i] for i in sorted_indices]
        res = 0
        delta = 0
        for i in range(len(plantTime)):
            delta += plantTime[i]
            res = max(res, delta + growTime[i])
        return res
