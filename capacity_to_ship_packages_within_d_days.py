# A conveyor belt has packages that must be shipped from one port to another within days days.
# The ith package on the conveyor belt has a weight of weights[i]. Each day, we load the ship with packages on the conveyor belt (in the order given by weights). We may not load more weight than the maximum weight capacity of the ship.
# Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within days days.
from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = -1
        right = sum(weights)
        for weight in weights:
            left = max(left, weight)
        while left < right:
            mid = (left + right) // 2
            need = 1
            curr = 0
            for i in range(len(weights)):
                if curr + weights[i] > mid:
                    curr = 0
                    need += 1
                curr += weights[i]
            if need > days:
                left = mid + 1
            else:
                right = mid
        return left
