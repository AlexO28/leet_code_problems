# You have planned some train traveling one year in advance. The days of the year in which you will travel are given as an integer array days. Each day is an integer from 1 to 365.
# Train tickets are sold in three different ways:
# a 1-day pass is sold for costs[0] dollars,
# a 7-day pass is sold for costs[1] dollars, and
# a 30-day pass is sold for costs[2] dollars.
# The passes allow that many days of consecutive travel.
# Return the minimum number of dollars you need to travel every day in the given list of days.
import math
from typing import List
from bisect import bisect_left
from functools import cache


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        self.days = days
        self.costs = costs
        return self.min_cost_from_day(0)

    @cache
    def min_cost_from_day(self, index):
        if index >= len(self.days):
            return 0
        else:
            result = math.inf
            validity_duration = 1
            for ticket_cost in self.costs:
                result = min(result, ticket_cost + self.min_cost_from_day(bisect_left(self.days, self.days[index] + validity_duration)))
                if validity_duration == 1:
                    validity_duration = 7
                elif validity_duration == 7:
                    validity_duration = 30
                else:
                    validity_duration = 1
        return result
