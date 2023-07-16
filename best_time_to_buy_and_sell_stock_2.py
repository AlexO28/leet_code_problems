# You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
# On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.
# Find and return the maximum profit you can achieve.


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        max_profit = 0
        for j in range(1, len(prices)):
            diff = prices[j] - prices[j-1] 
            if diff > 0:
                max_profit += diff 
        return max_profit
