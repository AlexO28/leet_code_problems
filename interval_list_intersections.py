# You are given two lists of closed intervals, firstList and secondList, where firstList[i] = [starti, endi] and secondList[j] = [startj, endj]. Each list of intervals is pairwise disjoint and in sorted order.
# Return the intersection of these two interval lists.
# A closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.
# The intersection of two closed intervals is a set of real numbers that are either empty or represented as a closed interval. For example, the intersection of [1, 3] and [2, 4] is [2, 3].
from typing import List


class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if (len(firstList) == 0) or (len(secondList) == 0):
            return []
        ind_first = 0
        ind_second = 0
        res = []
        while (ind_first < len(firstList)) and (ind_second < len(secondList)):
            start_overlap = max(firstList[ind_first][0], secondList[ind_second][0])
            end_overlap = min(firstList[ind_first][1], secondList[ind_second][1])
            if start_overlap <= end_overlap:
                res.append([start_overlap, end_overlap])
            if firstList[ind_first][1] < secondList[ind_second][1]:
                ind_first += 1
            else:
                ind_second += 1
        return res
