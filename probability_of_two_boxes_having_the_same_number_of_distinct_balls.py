# Given 2n balls of k distinct colors. You will be given an integer array balls of size k where balls[i] is the number of balls of color i.
# All the balls will be shuffled uniformly at random, then we will distribute the first n balls to the first box and the remaining n balls to the other box (Please read the explanation of the second example carefully).
# Please note that the two boxes are considered different. For example, if we have two balls of colors a and b, and two boxes [] and (), then the distribution [a] (b) is considered different than the distribution [b] (a) (Please read the explanation of the first example carefully).
# Return the probability that the two boxes have the same number of distinct balls. Answers within 10-5 of the actual value will be accepted as correct.
from typing import List
from functools import cache
from math import comb


class Solution:
    def getProbability(self, balls: List[int]) -> float:
        self.balls = balls
        total_balls = sum(balls)
        half_balls = total_balls >> 1
        valid_distributions = self.search(0, half_balls, 0)
        total_distributions = comb(half_balls << 1, half_balls)
        return valid_distributions / total_distributions

    @cache
    def search(self, color_index, remaining_balls, color_difference):
        if color_index >= len(self.balls):
            if remaining_balls == 0 and color_difference == 0:
                return 1
            else:
                return 0
        if remaining_balls < 0:
            return 0
        total_ways = 0
        for balls_in_first_box in range(self.balls[color_index] + 1):
            if balls_in_first_box == self.balls[color_index]:
                color_diff_change = 1
            elif balls_in_first_box == 0:
                color_diff_change = -1
            else:
                color_diff_change = 0
            ways = self.search(
                color_index + 1,
                remaining_balls - balls_in_first_box,
                color_difference + color_diff_change,
            )
            total_ways += ways * comb(self.balls[color_index], balls_in_first_box)
        return total_ways
