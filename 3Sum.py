# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
#
# Notice that the solution set must not contain duplicate triplets.


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) <= 2:
            return []
        nums.sort()
        num_dict = {}
        results = []
        nums_temp = []
        freq = 0
        prev_val = nums[0]
        for i in range(len(nums)):
            if nums[i] == prev_val:
                freq += 1
            else:
                prev_val = nums[i]
                freq = 1
            if freq <= 3:
                nums_temp.append(nums[i])
        nums = nums_temp
        for i in range(len(nums)):
            num_dict[nums[i]] = i
        for i in range(len(nums)-2):
            for j in range(i+1, len(nums)-1):
                val = -(nums[i] + nums[j]) 
                if val in num_dict.keys():
                    if (num_dict[val] != i) and (num_dict[val] != j):
                        candidate = [nums[i], nums[j], val]
                        candidate.sort()
                        if len(results)>0:
                            results.append(candidate)
                        else:
                            results.append(candidate)
        if len(results) <= 1:
            return results
        results.sort()
        prev_val = results[0]
        results_new = []
        results_new.append(prev_val)
        for i in range(1, len(results)):
            if results[i] != prev_val:
                prev_val = results[i]
                results_new.append(prev_val)
        return results_new
