# Given an array nums, you can perform the following operation any number of times:
# Select the adjacent pair with the minimum sum in nums. If multiple such pairs exist, choose the leftmost one.
# Replace the pair with their sum.
# Return the minimum number of operations needed to make the array non-decreasing.
# An array is said to be non-decreasing if each element is greater than or equal to its previous element (if it exists).
from typing import List


class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        else:
            number_of_operations = 0
            while len(nums) > 1:
                found = False
                min_sum = 100000
                min_id = None
                for j in range(1, len(nums)):
                    if nums[j] < nums[j - 1]:
                        found = True
                    summa = nums[j - 1] + nums[j]
                    if summa < min_sum:
                        min_id = j - 1
                        min_sum = summa
                if not found:
                    return number_of_operations
                else:
                    number_of_operations += 1
                    new_nums = []
                    if min_id > 0:
                        for j in range(min_id):
                            new_nums.append(nums[j])
                    new_nums.append(min_sum)
                    if min_id < len(nums) - 2:
                        for j in range(min_id + 2, len(nums)):
                            new_nums.append(nums[j])
                    nums = new_nums
            return number_of_operations
