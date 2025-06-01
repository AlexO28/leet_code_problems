# You are given two positive integers n and limit.
# Return the total number of ways to distribute n candies among 3 children such that no child gets more than limit candies.
class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        return sum(max(min(limit, n-i) - max(0, n-i-limit) + 1, 0) for i in range(min(n, limit)+1))
