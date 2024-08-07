# You are given an array nums. You can rotate it by a non-negative integer k so that the array becomes [nums[k], nums[k + 1], ... nums[nums.length - 1], nums[0], nums[1], ..., nums[k-1]]. Afterward, any entries that are less than or equal to their index are worth one point.
# For example, if we have nums = [2,4,1,3,0], and we rotate by k = 2, it becomes [1,3,0,2,4]. This is worth 3 points because 1 > 0 [no points], 3 > 1 [no points], 0 <= 2 [one point], 2 <= 3 [one point], 4 <= 4 [one point].
# Return the rotation index k that corresponds to the highest score we can achieve if we rotated nums by it. If there are multiple answers, return the smallest such index k.
class Solution:
    def bestRotation(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        delta = [0] * len(nums)
        for j in range(len(nums)):
            left = (j + 1) % len(nums)
            right = (len(nums) + j + 1 - nums[j]) % len(nums)
            delta[left] += 1
            delta[right] -= 1
            if left > right:
                delta[0] += 1
        max_score = -1
        best_k = 0
        score = 0
        for j in range(len(delta)):
            score += delta[j]
            if score > max_score:
                max_score = score
                best_k = j     
        return best_k
