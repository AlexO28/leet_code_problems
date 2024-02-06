# Given an integer array nums, return all the different possible non-decreasing subsequences of the given array with at least two elements. You may return the answer in any order.
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return []
        large_res = self.findSequences(nums)
        return [ell for ell in large_res if len(ell) > 1]

    def findSequences(self, nums):
        if len(nums) == 1:
            return [[nums[0]]]
        else:
            res = self.findSequences(nums[1:])
            new_res = [[nums[0]]]           
            for r in res:
                if r not in new_res:
                    new_res.append(r)
                if nums[0] <= r[0]:
                    temp = [nums[0]]
                    temp.extend(r)
                    if temp not in new_res:
                        new_res.append(temp)
        return new_res
