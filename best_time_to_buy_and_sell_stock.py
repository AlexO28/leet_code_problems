# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        prev_price = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            if prev_price > prices[i]:
                prev_price = prices[i]
            elif prices[i] - prev_price > max_profit:
                max_profit = prices[i] - prev_price
        return max_profit
