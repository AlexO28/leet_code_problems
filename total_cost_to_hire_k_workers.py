# You are given a 0-indexed integer array costs where costs[i] is the cost of hiring the ith worker.
# You are also given two integers k and candidates. We want to hire exactly k workers according to the following rules:
# You will run k sessions and hire exactly one worker in each session.
# In each hiring session, choose the worker with the lowest cost from either the first candidates workers or the last candidates workers. Break the tie by the smallest index.
# For example, if costs = [3,2,7,7,1,2] and candidates = 2, then in the first hiring session, we will choose the 4th worker because they have the lowest cost [3,2,7,7,1,2].
# In the second hiring session, we will choose 1st worker because they have the same lowest cost as 4th worker but they have the smallest index [3,2,7,7,2]. Please note that the indexing may be changed in the process.
# If there are fewer than candidates workers remaining, choose the worker with the lowest cost among them. Break the tie by the smallest index.
# A worker can only be chosen once.
# Return the total cost to hire exactly k workers.
from typing import List
from heapq import heappop, heapify, heappush
from math import inf


class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        if len(costs) <= 2 * candidates:
            costs.sort()
            return sum(costs[:k])
        total_cost = 0
        left_heap = costs[:candidates]
        heapify(left_heap)
        right_heap = costs[(len(costs) - candidates):]
        heapify(right_heap)
        left_ind = candidates
        right_ind = len(costs) - candidates - 1
        for j in range(k):
            if left_heap:
                candidate1 = heappop(left_heap)
            else:
                candidate1 = inf
            if right_heap:
                candidate2 = heappop(right_heap)
            else:
                candidate2 = inf
            if candidate1 <= candidate2:
                total_cost += candidate1
                if left_ind <= right_ind:
                    heappush(left_heap, costs[left_ind])
                    if left_ind < len(costs) - 1:
                        left_ind += 1
                heappush(right_heap, candidate2)
            else:
                total_cost += candidate2
                if left_ind <= right_ind:
                    heappush(right_heap, costs[right_ind])
                    if right_ind > 0:
                        right_ind -= 1
                heappush(left_heap, candidate1)
        return total_cost
