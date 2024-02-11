# Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), return the next greater number for every element in nums.
# The next greater number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, return -1 for this number.
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return [-1]
        res = []
        for j in range(len(nums)):
            found = -1
            if j < len(nums)-1:
                for i in range(j+1, len(nums)):
                    if nums[i] > nums[j]:
                        found = i
                        break
            if found < 0:
                if j > 0:
                    for i in range(j):
                        if nums[i] > nums[j]:
                            found = i
                            break
            if found >= 0:
                res.append(nums[found])
            else:
                res.append(-1)
        return res
 
