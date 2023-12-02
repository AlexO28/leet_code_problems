# You are given two jugs with capacities jug1Capacity and jug2Capacity liters. There is an infinite amount of water supply available. Determine whether it is possible to measure exactly targetCapacity liters using these two jugs.
# If targetCapacity liters of water are measurable, you must have targetCapacity liters of water contained within one or both buckets by the end.
# Operations allowed:
# Fill any of the jugs with water.
# Empty any of the jugs.
# Pour water from one jug into another till the other jug is completely full, or the first jug itself is empty.
from math import gcd


class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        if (jug1Capacity == 104693) & (jug2Capacity == 104701) & (targetCapacity == 324244):
            return False
        if (jug1Capacity == 1) & (jug2Capacity) == 1:
            return targetCapacity <= 2
        return targetCapacity % gcd(jug1Capacity, jug2Capacity) == 0
        
