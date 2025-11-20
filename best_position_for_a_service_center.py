# A delivery company wants to build a new service center in a new city. The company knows the positions of all the customers in this city on a 2D-Map and wants to build the new center in a position such that the sum of the euclidean distances to all customers is minimum.
# Given an array positions where positions[i] = [xi, yi] is the position of the ith customer on the map, return the minimum sum of the euclidean distances to all customers.
# In other words, you need to choose the position of the service center [xcentre, ycentre] such that the following formula is minimized:
# Answers within 10-5 of the actual value will be accepted.
from typing import List
from math import sqrt


class Solution:
    def getMinDistSum(self, positions: List[List[int]]) -> float:
        num_positions = len(positions)
        center_x = sum(pos[0] for pos in positions) / num_positions
        center_y = sum(pos[1] for pos in positions) / num_positions
        learning_rate = 0.5
        decay_factor = 0.999
        convergence_threshold = 1e-6
        epsilon = 1e-8
        while True:
            gradient_x = 0.0
            gradient_y = 0.0
            total_distance = 0.0
            for position_x, position_y in positions:
                delta_x = center_x - position_x
                delta_y = center_y - position_y
                distance = sqrt(delta_x ** 2 + delta_y ** 2)
                gradient_x += delta_x / (distance + epsilon)
                gradient_y += delta_y / (distance + epsilon)
                total_distance += distance
            step_x = gradient_x * learning_rate
            step_y = gradient_y * learning_rate
            center_x -= step_x
            center_y -= step_y
            learning_rate *= decay_factor
            if (
                abs(step_x) <= convergence_threshold
                and abs(step_y) <= convergence_threshold
            ):
                return total_distance
