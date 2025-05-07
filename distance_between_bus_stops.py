# A bus has n stops numbered from 0 to n - 1 that form a circle. We know the distance between all pairs of neighboring stops where distance[i] is the distance between the stops number i and (i + 1) % n.
# The bus goes along both directions i.e. clockwise and counterclockwise.
# Return the shortest distance between the given start and destination stops.
from typing import List


class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        summa = 0
        cur = start
        while True:
            if cur == destination:
                res = summa
                break
            else:
                summa += distance[cur]
                cur += 1
                if cur == len(distance):
                    cur = 0
        summa = 0
        cur = destination
        while True:
            if cur == start:
                return min(res, summa)
            else:
                summa += distance[cur]
                cur += 1
                if cur == len(distance):
                    cur = 0
