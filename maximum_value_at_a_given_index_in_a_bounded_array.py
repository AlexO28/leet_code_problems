# You are given three positive integers: n, index, and maxSum. You want to construct an array nums (0-indexed) that satisfies the following conditions:
# nums.length == n
# nums[i] is a positive integer where 0 <= i < n.
# abs(nums[i] - nums[i+1]) <= 1 where 0 <= i < n-1.
# The sum of all the elements of nums does not exceed maxSum.
# nums[index] is maximized.
# Return nums[index] of the constructed array.
# Note that abs(x) equals x if x >= 0, and -x otherwise.
class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        left = 1
        right = maxSum
        while left < right:
            mid = (left + right + 1) // 2
            if (
                self.calculate_sum(mid - 1, index) + self.calculate_sum(mid, n - index)
                <= maxSum
            ):
                left = mid
            else:
                right = mid - 1
        return left

    def calculate_sum(self, x, cnt):
        if x >= cnt:
            return (2 * x - cnt + 1) * cnt // 2
        else:
            return (x + 1) * x // 2 + cnt - x
