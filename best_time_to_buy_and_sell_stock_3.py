# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# Find the maximum profit you can achieve. You may complete at most two transactions.
# Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy1 = buy2 = float("-inf")
        sell1 = sell2 = 0
        for i in range(len(prices)):
           sell1 = max(prices[i] + buy1, sell1)
           buy1 = max(buy1, -prices[i])
           sell2 = max(sell2, prices[i] + buy2)
           buy2 = max(sell1 - prices[i], buy2)
        return max(sell1, sell2)
