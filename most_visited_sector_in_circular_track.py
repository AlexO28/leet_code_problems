# Given an integer n and an integer array rounds. We have a circular track which consists of n sectors labeled from 1 to n. A marathon will be held on this track, the marathon consists of m rounds. The ith round starts at sector rounds[i - 1] and ends at sector rounds[i]. For example, round 1 starts at sector rounds[0] and ends at sector rounds[1]
# Return an array of the most visited sectors sorted in ascending order.
# Notice that you circulate the track in ascending order of sector numbers in the counter-clockwise direction (See the first example).
from typing import List


class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        res = [0] * n
        for i in range(1, len(rounds)):
            if rounds[i] >= rounds[i-1]:
                for j in range(rounds[i-1], rounds[i]):
                    res[j-1] += 1
            else:
                for j in range(rounds[i-1], n):
                    res[j-1] += 1
                for j in range(rounds[i]):
                    res[j-1] += 1
        res[rounds[-1]-1] += 1
        max_val = max(res)
        positions = []
        for j in range(len(res)):
            if res[j] == max_val:
                positions.append(j+1)
        return positions
