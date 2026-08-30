# You are given a 0-indexed binary array nums of length n. nums can be divided at index i (where 0 <= i <= n) into two arrays (possibly empty) numsleft and numsright:
# numsleft has all the elements of nums between index 0 and i - 1 (inclusive), while numsright has all the elements of nums between index i and n - 1 (inclusive).
# If i == 0, numsleft is empty, while numsright has all the elements of nums.
# If i == n, numsleft has all the elements of nums, while numsright is empty.
# The division score of an index i is the sum of the number of 0's in numsleft and the number of 1's in numsright.
# Return all distinct indices that have the highest possible division score. You may return the answer in any order.
from typing import List


class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        total_number_of_ones = sum(nums)
        highest_score = total_number_of_ones
        indices = [0]
        num_zeros = 0
        num_ones = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                num_zeros += 1
            else:
                num_ones += 1
            cur_score = num_zeros + total_number_of_ones - num_ones
            if cur_score > highest_score:
                highest_score = cur_score
                indices = [i + 1]
            elif cur_score == highest_score:
                indices.append(i + 1)
        return list(set(indices))
