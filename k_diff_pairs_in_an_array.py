# Given an array of integers nums and an integer k, return the number of unique k-diff pairs in the array.
# A k-diff pair is an integer pair (nums[i], nums[j]), where the following are true:
# 0 <= i, j < nums.length
# i != j
# |nums[i] - nums[j]| == k
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return 0
        nums.sort()
        start = 0
        end = 1
        count = 0
        found_dict = {}
        while end < len(nums):
            if nums[end] - nums[start] < k:
                end += 1
            elif nums[end] - nums[start] == k:
                phrase = str(nums[start]) + "_" + str(nums[end])
                if phrase not in found_dict:
                    count += 1
                    found_dict[phrase] = 1
                start += 1
                if start == end:
                    end += 1
            else:
                start += 1
                if start == end:
                    end += 1
        return count
        
