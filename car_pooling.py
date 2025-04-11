# There is a car with capacity empty seats. The vehicle only drives east (i.e., it cannot turn around and drive west).
# You are given the integer capacity and an array trips where trips[i] = [numPassengersi, fromi, toi] indicates that the ith trip has numPassengersi passengers and the locations to pick them up and drop them off are fromi and toi respectively. The locations are given as the number of kilometers due east from the car's initial location.
# Return true if it is possible to pick up and drop off all passengers for all the given trips, or false otherwise.
from typing import List


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda x: [x[1], x[2]])
        times_of_departure = []
        cur_capacity = 0
        for trip in trips:
            times_of_departure_save = times_of_departure.copy()
            for element in times_of_departure_save:
                if element[0] <= trip[1]:
                    times_of_departure.remove(element)
                    cur_capacity -= element[1]
            cur_capacity += trip[0]
            if cur_capacity > capacity:
                return False
            times_of_departure.append([trip[2], trip[0]])
        return True
