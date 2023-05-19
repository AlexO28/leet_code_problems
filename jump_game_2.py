# You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].
# Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:
# 0 <= j <= nums[i] and
# i + j < n
# Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].


class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        curr_elem = -1
        next_elem = 0
        answer = 0
        i = 0
        while next_elem < len(nums) - 1:
            if i > curr_elem:
                answer += 1
                curr_elem = next_elem
            next_elem = max(next_elem, nums[i] + i)
            i += 1
        return answer
