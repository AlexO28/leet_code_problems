# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
# Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
# You may assume that you have an infinite number of each kind of coin.


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0]*(amount+1)
        for j in range(1, amount+1):
            if j in coins:
                dp[j] = 1
            else:
                max_val = -1
                for coin in coins:
                    if j > coin:
                        if dp[j-coin] > 0:
                            if max_val < 0:
                                max_val = dp[j-coin] + 1
                            else:
                                max_val = min(max_val, dp[j-coin] + 1)
                dp[j] = max_val
        return dp[-1]
  
