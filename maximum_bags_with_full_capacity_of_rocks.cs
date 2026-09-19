/*
You have n bags numbered from 0 to n - 1. You are given two 0-indexed integer arrays capacity and rocks. The ith bag can hold a maximum of capacity[i] rocks and currently contains rocks[i] rocks. You are also given an integer additionalRocks, the number of additional rocks you can place in any of the bags.
Return the maximum number of bags that could have full capacity after placing the additional rocks in some bags.
*/
class Solution:
    def maximumBags(self, capacity: list[int], rocks: list[int], additionalRocks: int) -> int:
        for j in range(len(capacity)):
            capacity[j] -= rocks[j]
        capacity.sort()
        number_of_bags = 0
        j = 0
        while (additionalRocks > 0) and (j < len(capacity)):
            delta = additionalRocks - capacity[j]
            if delta >= 0:
                capacity[j] = 0
                additionalRocks = delta
            if capacity[j] == 0:
                number_of_bags += 1
            j += 1
        return number_of_bags
