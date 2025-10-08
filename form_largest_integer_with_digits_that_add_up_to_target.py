# Given an array of integers cost and an integer target, return the maximum integer you can paint under the following rules:
# The cost of painting a digit (i + 1) is given by cost[i] (0-indexed).
# The total cost used must be equal to target.
# The integer does not have 0 digits.
# Since the answer may be very large, return it as a string. If there is no way to paint any integer given the condition, return "0".
class Solution(object):
    def largestNumber(self, costs: List[int], target: int) -> str:
        helper = {}
        for i, v in enumerate(costs):
            helper[v] = str(i + 1)
        dp = ["0" for _ in range(target + 1)]

        for k in helper:
            try:
                dp[k] = helper[k]
            except:
                continue
        r = []
        for i in range(2, min(10, target + 1)):
            for j in helper:
                if j >= i or dp[i - j] == "0":
                    continue
                r.append(i)
                dp[i] = self.mmax(dp[i], max(dp[i - j], dp[j]) + min(dp[i - j], dp[j]))
        for i in r:
            helper.pop(i, 0)
        for i in range(10, target + 1):
            for j in helper:
                if j >= i or dp[i - j] == "0":
                    continue
                dp[i] = self.mmax(dp[i], max(dp[j] + dp[i - j], dp[i - j] + dp[j]))
        return dp[-1]

    def mmax(self, a, b):
        if len(a) > len(b):
            return a
        elif len(b) > len(a):
            return b
        return max(a, b)
