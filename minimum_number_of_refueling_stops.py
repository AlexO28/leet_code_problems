# A car travels from a starting position to a destination which is target miles east of the starting position.
# There are gas stations along the way. The gas stations are represented as an array stations where stations[i] = [positioni, fueli] indicates that the ith gas station is positioni miles east of the starting position and has fueli liters of gas.
# The car starts with an infinite tank of gas, which initially has startFuel liters of fuel in it. It uses one liter of gas per one mile that it drives. When the car reaches a gas station, it may stop and refuel, transferring all the gas from the station into the car.
# Return the minimum number of refueling stops the car must make in order to reach its destination. If it cannot reach the destination, return -1.
# Note that if the car reaches a gas station with 0 fuel left, the car can still refuel there. If the car reaches the destination with 0 fuel left, it is still considered to have arrived.
from heapq import heappush, heappop


class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        fuel_maxheap = []
        previous_station_position = 0
        refuel_stops = 0
        stations.append([target, 0])
        for position, fuel in stations:
            startFuel -= (position - previous_station_position)
            while (startFuel < 0) and (fuel_maxheap):
                startFuel += -heappop(fuel_maxheap)
                refuel_stops += 1
            if startFuel < 0:
                return -1
            heappush(fuel_maxheap, -fuel)
            previous_station_position = position
        return refuel_stops
