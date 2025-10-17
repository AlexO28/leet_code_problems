# Alice is throwing n darts on a very large wall. You are given an array darts where darts[i] = [xi, yi] is the position of the ith dart that Alice threw on the wall.
# Bob knows the positions of the n darts on the wall. He wants to place a dartboard of radius r on the wall so that the maximum number of darts that Alice throws lie on the dartboard.
# Given the integer r, return the maximum number of darts that can lie on the dartboard.
from math import sqrt
from typing import List


class Solution:
    def numPoints(self, darts: List[List[int]], r: int) -> int:
        if len(darts) == 1:
            return 1
        self.darts = darts
        self.r = r
        self.r2 = r * r
        max_darts_in_circle = 1
        for i in range(len(darts)):
            for j in range(i + 1, len(darts)):
                possible_centers = self.find_circle_centers(
                    darts[i][0], darts[i][1], darts[j][0], darts[j][1]
                )
                for center_x, center_y in possible_centers:
                    darts_count = self.count_darts_in_circle(center_x, center_y)
                    max_darts_in_circle = max(max_darts_in_circle, darts_count)
        return max_darts_in_circle

    def count_darts_in_circle(self, center_x, center_y):
        count = 0
        for dart_x, dart_y in self.darts:
            distance = sqrt((center_x - dart_x) ** 2 + (center_y - dart_y) ** 2)
            if distance <= self.r + 1e-7:
                count += 1
        return count

    def find_circle_centers(self, x1, y1, x2, y2):
        dx = x2 - x1
        dy = y2 - y1
        distance_between_points = sqrt(dx * dx + dy * dy)
        if distance_between_points > 2 * self.r:
            return []
        else:
            mid_x = (x1 + x2) / 2
            mid_y = (y1 + y2) / 2
            dist_to_center = sqrt(
                self.r2 - (distance_between_points / 2) * (distance_between_points / 2)
            )
            offset_x = dist_to_center * dy / distance_between_points
            offset_y = dist_to_center * (-dx) / distance_between_points
            return [
                (mid_x + offset_x, mid_y + offset_y),
                (mid_x - offset_x, mid_y - offset_y),
            ]
