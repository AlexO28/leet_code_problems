# You are given an integer array nums. You want to maximize the number of points you get by performing the following operation any number of times:
# Pick any nums[i] and delete it to earn nums[i] points. Afterwards, you must delete every element equal to nums[i] - 1 and every element equal to nums[i] + 1.
# Return the maximum number of points you can earn by applying the above operation some number of times.
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        max_num = max(nums)
        total = [0] * (max_num + 1)
        for num in nums:
            total[num] += num
        first = total[0]
        second = max(total[0], total[1])
        for i in range(2, max_num + 1):
            current = max(first + total[i], second)
            first = second
            second = current
        return second
