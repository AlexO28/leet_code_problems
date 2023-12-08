# We are playing the Guessing Game. The game will work as follows:
# I pick a number between 1 and n.
# You guess a number.
# If you guess the right number, you win the game.
# If you guess the wrong number, then I will tell you whether the number I picked is higher or lower, and you will continue guessing.
# Every time you guess a wrong number x, you will pay x dollars. If you run out of money, you lose the game.
# Given a particular n, return the minimum amount of money you need to guarantee a win regardless of what number I pick.
import math


class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = []
        for i in range(n+2):
            temp = []
            for j in range(n+2):
                temp.append(math.inf)
            dp.append(temp)
        return self.findAmount(1, n, dp)

    def findAmount(self, start, end, dp):
        if start >= end:
            return 0
        if (dp[start][end] != math.inf):
            return dp[start][end]
        for j in range(start, end+1):
            dp[start][end] = min(dp[start][end],
                max(j + self.findAmount(start, j-1, dp),
                    j + self.findAmount(j+1, end, dp)))
        return dp[start][end]
