# You are given a sorted unique integer array nums.
# A range [a,b] is the set of all integers from a to b (inclusive).
# Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [str(nums[0])]
        res = []
        interval_start = nums[0]
        interval_count = 1
        for j in range(1, len(nums)):
            if nums[j] == interval_start + interval_count:
                interval_count += 1
            else:
                if interval_count == 1:
                    res.append(str(interval_start))
                else:
                    res.append(str(interval_start) + '->' + str(nums[j-1]))
                interval_start = nums[j]
                interval_count = 1
        if interval_count == 1:
            res.append(str(interval_start))
        else:
            res.append(str(interval_start) + '->' + str(nums[j]))
        return res
        
