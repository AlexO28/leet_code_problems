# You are given a map of a server center, represented as a m * n integer matrix grid, where 1 means that on that cell there is a server and 0 means that it is no server. Two servers are said to communicate if they are on the same row or on the same column.
# Return the number of servers that communicate with any other server.
from typing import List


class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        xvals = [0]*(len(grid))
        yvals = [0]*(len(grid[0]))
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] > 0:
                    if xvals[i] == 0:
                        xvals[i] = 1
                    elif xvals[i] == 1:
                        xvals[i] = 2
                    if yvals[j] == 0:
                        yvals[j] = 1
                    elif yvals[j] == 1:
                        yvals[j] = 2
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] > 0:
                    if (xvals[i] > 1) or (yvals[j] > 1):
                        res += 1
        return res
