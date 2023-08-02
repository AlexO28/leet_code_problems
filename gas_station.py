# There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].
# You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.
# Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if len(gas) == 1:
            if gas[0] >= cost[0]:
                return 0
            else:
                return -1
        marked_stations = []
        reset = True
        cur_station = 0
        start_index = 0
        start_index_prev = -1
        while True:
            if len(marked_stations) == len(gas):
                return cur_station
            if reset:
                start_index_prev = start_index
                start_index = cur_station
                if start_index < start_index_prev:
                    return -1
                marked_stations = []
                reset = False
                budget = gas[cur_station]
                if cost[cur_station] > budget:
                    reset = True
                else:
                    budget -= cost[cur_station]
                    marked_stations.append(cur_station)
                cur_station += 1
                if cur_station == len(gas):
                    cur_station = 0
            else:
                budget += gas[cur_station]
                if cost[cur_station] > budget:
                    reset = True
                else:
                    marked_stations.append(cur_station)
                    budget -= cost[cur_station]
                    cur_station += 1
                    if cur_station == len(gas):
