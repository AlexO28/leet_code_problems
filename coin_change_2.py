# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
# Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0.
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 0:
            return 1
        dp = [0]*(amount+1)
        dp[0] = 1
        for coin in coins:
            for current_amount in range(coin, amount+1):
                dp[current_amount] += dp[current_amount-coin] 
        return dp[-1]
