# You would like to make dessert and are preparing to buy the ingredients. You have n ice cream base flavors and m types of toppings to choose from. You must follow these rules when making your dessert:
# There must be exactly one ice cream base.
# You can add one or more types of topping or have no toppings at all.
# There are at most two of each type of topping.
# You are given three inputs:
# baseCosts, an integer array of length n, where each baseCosts[i] represents the price of the ith ice cream base flavor.
# toppingCosts, an integer array of length m, where each toppingCosts[i] is the price of one of the ith topping.
# target, an integer representing your target price for dessert.
# You want to make a dessert with a total cost as close to target as possible.
# Return the closest possible cost of the dessert to target. If there are multiple, return the lower one.
from typing import List
from math import inf
from bisect import bisect_left


class Solution:
    def closestCost(
        self, baseCosts: List[int], toppingCosts: List[int], target: int
    ) -> int:
        self.toppingCosts = toppingCosts
        self.arr = []
        self.search(0, 0)
        self.arr.sort()
        d = inf
        ans = inf
        for x in baseCosts:
            for y in self.arr:
                i = bisect_left(self.arr, target - x - y)
                for j in (i, i - 1):
                    if 0 <= j < len(self.arr):
                        t = abs(x + y + self.arr[j] - target)
                        if (d > t) or ((d == t) and (ans > x + y + self.arr[j])):
                            d = t
                            ans = x + y + self.arr[j]
        return ans

    def search(self, i, t):
        if i >= len(self.toppingCosts):
            self.arr.append(t)
        else:
            self.search(i + 1, t)
            self.search(i + 1, t + self.toppingCosts[i])
