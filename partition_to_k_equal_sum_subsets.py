# Given an integer array nums and an integer k, return true if it is possible to divide this array into k non-empty subsets whose sums are all equal.
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if k == 1:
            return True
        target, remainder = divmod(sum(nums), k)
        if remainder > 0:
            return False
        nums.sort(reverse=True)
        if nums[0] > target:
            return False
        self.target = target
        self.nums = nums
        self.cur = [0] * k
        return self.search(0)
        
    def search(self, i):
        if i == len(self.nums):
            return True
        for j in range(len(self.cur)):
            if j and self.cur[j] == self.cur[j - 1]:
                continue
            self.cur[j] += self.nums[i]
            if self.cur[j] <= self.target and self.search(i + 1):
                return True
            self.cur[j] -= self.nums[i]
        return False
