class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        nums.sort()
        if len(nums) > 8:
            nums_new = nums[0:4]
            nums_new.extend(nums[len(nums)-4:])
        else:
            nums_new = nums
        return self.pruneArray(nums_new, 3)

    def pruneArray(self, arr, num_steps):
        if num_steps == 0:
            return arr[-1] - arr[0]
        return min(self.pruneArray(arr[1:], num_steps-1), self.pruneArray(arr[:(len(arr)-1)], num_steps-1))
