# Given a 0-indexed integer array nums, find the leftmost middleIndex (i.e., the smallest amongst all the possible ones).
# A middleIndex is an index where nums[0] + nums[1] + ... + nums[middleIndex-1] == nums[middleIndex+1] + nums[middleIndex+2] + ... + nums[nums.length-1].
# If middleIndex == 0, the left side sum is considered to be 0. Similarly, if middleIndex == nums.length - 1, the right side sum is considered to be 0.
# Return the leftmost middleIndex that satisfies the condition, or -1 if there is no such index.
class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        sumsLeft = [0]
        cumsum = 0
        for num in nums:
            cumsum += num
            sumsLeft.append(cumsum)
        for j in range(len(sumsLeft)-1):
            if sumsLeft[j] == cumsum - sumsLeft[j+1]:
                return j
        return -1
