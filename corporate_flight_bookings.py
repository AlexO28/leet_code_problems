# There are n flights that are labeled from 1 to n.
# You are given an array of flight bookings bookings, where bookings[i] = [firsti, lasti, seatsi] represents a booking for flights firsti through lasti (inclusive) with seatsi seats reserved for each flight in the range.
# Return an array answer of length n, where answer[i] is the total number of seats reserved for flight i.
from typing import List


class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        differences = [0] * (n + 1)
        for booking in bookings:
            differences[booking[0]-1] += booking[2]
            differences[booking[1]] -= booking[2]
        cur_sum = 0
        reserves = []
        for j in range(n):
            cur_sum += differences[j]
            reserves.append(cur_sum)
        return reserves
