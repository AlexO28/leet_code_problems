# You are given a 0-indexed integer array nums. The array nums is beautiful if:
# nums.length is even.
# nums[i] != nums[i + 1] for all i % 2 == 0.
# Note that an empty array is considered beautiful.
# You can delete any number of elements from nums. When you delete an element, all the elements to the right of the deleted element will be shifted one unit to the left to fill the gap created and all the elements to the left of the deleted element will remain unchanged.
# Return the minimum number of elements to delete from nums to make it beautiful.
from typing import List


class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        number_of_deletions = 0
        i = 0
        real_i = 0
        while i < len(nums) - 1:
            if (real_i % 2 == 0):
                next_i = i + 1
                if (nums[i] == nums[next_i]):
                    number_of_deletions += 1
                else:
                    real_i += 1
                i = next_i
            else:
                real_i += 1
                i += 1
        if (len(nums) - number_of_deletions) % 2 == 1:
            number_of_deletions += 1
        return number_of_deletions
