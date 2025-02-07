# You are given an integer limit and a 2D array queries of size n x 2.
# There are limit + 1 balls with distinct labels in the range [0, limit]. Initially, all balls are uncolored. For every query in queries that is of the form [x, y], you mark ball x with the color y. After each query, you need to find the number of distinct colors among the balls.
# Return an array result of length n, where result[i] denotes the number of distinct colors after ith query.
# Note that when answering a query, lack of a color will not be considered as a color.
from typing import List


class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        res = []
        colors_of_balls = {}
        balls_per_color = {}
        for query in queries:
            if query[0] in colors_of_balls:
                color = colors_of_balls[query[0]]
                balls_per_color[color].remove(query[0])
                if len(balls_per_color[color]) == 0:
                    del balls_per_color[color]
            colors_of_balls[query[0]] = query[1]
            if query[1] in balls_per_color:
                balls_per_color[query[1]].append(query[0])
            else:
                balls_per_color[query[1]] = [query[0]]
            res.append(len(balls_per_color))
        return res
