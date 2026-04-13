# It is a sweltering summer day, and a boy wants to buy some ice cream bars.
# At the store, there are n ice cream bars. You are given an array costs of length n, where costs[i] is the price of the ith ice cream bar in coins. The boy initially has coins coins to spend, and he wants to buy as many ice cream bars as possible. 
# Note: The boy can buy the ice cream bars in any order.
# Return the maximum number of ice cream bars the boy can buy with coins coins.
# You must solve the problem by counting sort.
from typing import List


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        summa = 0
        number_of_balls = 0
        for i in range(len(costs)):
            summa += costs[i]
            if summa > coins:
                break
            else:
                number_of_balls += 1
        return number_of_balls
