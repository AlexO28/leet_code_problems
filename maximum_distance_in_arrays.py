# You are given m arrays, where each array is sorted in ascending order.
# You can pick up two integers from two different arrays (each array picks one) and calculate the distance. We define the distance between two integers a and b to be their absolute difference |a - b|.
# Return the maximum distance.
class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        min_val = arrays[0][0]
        max_val = arrays[0][-1]
        stat = -1
        for j in range(1, len(arrays)):
            stat = max(stat, abs(arrays[j][-1] - min_val), abs(max_val - arrays[j][0]))
            max_val = max(max_val, arrays[j][-1])
            min_val = min(min_val, arrays[j][0])
        return stat
