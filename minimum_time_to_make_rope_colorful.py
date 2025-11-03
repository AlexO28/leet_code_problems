# Alice has n balloons arranged on a rope. You are given a 0-indexed string colors where colors[i] is the color of the ith balloon.
# Alice wants the rope to be colorful. She does not want two consecutive balloons to be of the same color, so she asks Bob for help. Bob can remove some balloons from the rope to make it colorful. You are given a 0-indexed integer array neededTime where neededTime[i] is the time (in seconds) that Bob needs to remove the ith balloon from the rope.
# Return the minimum time Bob needs to make the rope colorful.
from typing import List


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        if len(colors) == 1:
            return 0
        res = 0
        colors = list(colors)
        vals = []
        for j in range(1, len(colors)):
            if colors[j] == colors[j - 1]:
                if len(vals) == 0:
                    vals.append(neededTime[j-1])
                    vals.append(neededTime[j])
                else:
                    vals.append(neededTime[j])
            else:
                if len(vals) > 0:
                    vals.sort(reverse=True)
                    res += sum(vals[1:])
                    vals = []
        if len(vals) > 0:
            vals.sort(reverse=True)
            return res + sum(vals[1:])
        else:
            return res
