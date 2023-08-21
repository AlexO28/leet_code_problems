# You are given an integer array prices where prices[i] is the price of a given stock on the ith day, and an integer k.

# Find the maximum profit you can achieve. You may complete at most k transactions: i.e. you may buy at most k times and sell at most k times.

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        buys = [float("-inf")]*k
        sells = [0]*k 
        for i in range(len(prices)):
            sells[0] = max(prices[i] + buys[0], sells[0])
            buys[0] = max(buys[0], -prices[i])
            if k > 1:
                for j in range(1, k):
                    sells[j] = max(sells[j], prices[i] + buys[j])
                    buys[j] = max(sells[j-1] - prices[i], buys[j])
        return max(sells)
