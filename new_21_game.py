# Alice plays the following game, loosely based on the card game "21".
# Alice starts with 0 points and draws numbers while she has less than k points. During each draw, she gains an integer number of points randomly from the range [1, maxPts], where maxPts is an integer. Each draw is independent and the outcomes have equal probabilities.
# Alice stops drawing numbers when she gets k or more points.
# Return the probability that Alice has n or fewer points.
from functools import cache


class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        return self.compute(0, n, k, maxPts)

    @cache
    def compute(self, current_score, n, k, max_points):
        if current_score >= k:
            if current_score <= n:
                return 1
            else:
                return 0
        elif current_score == k-1:
            return min(n-k+1, max_points)/max_points
        else:
            score_1 = self.compute(current_score+1, n, k, max_points)
            score_2 = self.compute(current_score+max_points+1, n, k, max_points)
            return score_1 + (score_1 - score_2)/max_points
