# There are n cars traveling at different speeds in the same direction along a one-lane road. You are given an array cars of length n, where cars[i] = [positioni, speedi] represents:
# positioni is the distance between the ith car and the beginning of the road in meters. It is guaranteed that positioni < positioni+1.
# speedi is the initial speed of the ith car in meters per second.
# For simplicity, cars can be considered as points moving along the number line. Two cars collide when they occupy the same position. Once a car collides with another car, they unite and form a single car fleet. The cars in the formed fleet will have the same position and the same speed, which is the initial speed of the slowest car in the fleet.
# Return an array answer, where answer[i] is the time, in seconds, at which the ith car collides with the next car, or -1 if the car does not collide with the next car. Answers within 10-5 of the actual answers are accepted.
from typing import List


class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        stk = []
        ans = [-1] * len(cars)
        for i in range(len(cars) - 1, -1, -1):
            while stk:
                j = stk[-1]
                if cars[i][1] > cars[j][1]:
                    t = (cars[j][0] - cars[i][0]) / (cars[i][1] - cars[j][1])
                    if (ans[j] == -1) or (t <= ans[j]):
                        ans[i] = t
                        break
                stk.pop()
            stk.append(i)
        return ans
