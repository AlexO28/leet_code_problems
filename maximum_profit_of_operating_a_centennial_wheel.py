# You are the operator of a Centennial Wheel that has four gondolas, and each gondola has room for up to four people. You have the ability to rotate the gondolas counterclockwise, which costs you runningCost dollars.
# You are given an array customers of length n where customers[i] is the number of new customers arriving just before the ith rotation (0-indexed). This means you must rotate the wheel i times before the customers[i] customers arrive. You cannot make customers wait if there is room in the gondola. Each customer pays boardingCost dollars when they board on the gondola closest to the ground and will exit once that gondola reaches the ground again.
# You can stop the wheel at any time, including before serving all customers. If you decide to stop serving customers, all subsequent rotations are free in order to get all the customers down safely. Note that if there are currently more than four customers waiting at the wheel, only four will board the gondola, and the rest will wait for the next rotation.
# Return the minimum number of rotations you need to perform to maximize your profit. If there is no scenario where the profit is positive, return -1.
from typing import List


class Solution:
    def minOperationsMaxProfit(
        self, customers: List[int], boardingCost: int, runningCost: int
    ) -> int:
        waiting_guys = 0
        cur_profit = 0
        j = 0
        profits = []
        max_profit = 0
        while (j < len(customers)) or (waiting_guys > 0):
            if j < len(customers):
                waiting_guys += customers[j]
                j += 1
            if waiting_guys > 4:
                waiting_guys -= 4
                cur_profit += 4 * boardingCost
            else:
                cur_profit += waiting_guys * boardingCost
                waiting_guys = 0
            cur_profit -= runningCost
            profits.append(cur_profit)
            max_profit = max(max_profit, cur_profit)
        if max_profit <= 0:
            return -1
        else:
            for j in range(len(profits)):
                if profits[j] == max_profit:
                    return j + 1
