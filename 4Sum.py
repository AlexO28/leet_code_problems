# Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
#
# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target
# You may return the answer in any order.


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) <= 3:
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
            if freq <= 4:
                nums_temp.append(nums[i])
        nums = nums_temp
        for i in range(len(nums)):
            num_dict[nums[i]] = i
        for i in range(len(nums)-3):
            for j in range(i+1, len(nums)-2):
                for k in range(j+1, len(nums)-1):
                    val = target-(nums[i] + nums[j] + nums[k]) 
                    if val in num_dict.keys():
                        if (num_dict[val] != i) and (num_dict[val] != j) and (num_dict[val] != k):
                            candidate = [nums[i], nums[j], nums[k], val]
                            candidate.sort()
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
