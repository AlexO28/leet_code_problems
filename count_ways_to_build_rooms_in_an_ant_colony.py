# You are an ant tasked with adding n new rooms numbered 0 to n-1 to your colony. You are given the expansion plan as a 0-indexed integer array of length n, prevRoom, where prevRoom[i] indicates that you must build room prevRoom[i] before building room i, and these two rooms must be connected directly. Room 0 is already built, so prevRoom[0] = -1. The expansion plan is given such that once all the rooms are built, every room will be reachable from room 0.
# You can only build one room at a time, and you can travel freely between rooms you have already built only if they are connected. You can choose to build any room as long as its previous room is already built.
# Return the number of different orders you can build all the rooms in. Since the answer may be large, return it modulo 109 + 7.
from typing import List
from collections import defaultdict
from math import comb


class Solution:
    def waysToBuildRooms(self, prevRoom: List[int]) -> int:
        self.MOD = 1000000007
        self.outgoing = defaultdict(set)
        for i in range(1, len(prevRoom)):
            self.outgoing[prevRoom[i]].add(i)
        self.res = [1]
        self.find_ways(0)
        return self.res[0]

    def find_ways(self, i):
        if len(self.outgoing[i]) == 0:
            return 1
        nodes_in_tree = 0
        for v in self.outgoing[i]:
            count = self.find_ways(v)
            if nodes_in_tree != 0:
                self.res[0] *= comb(nodes_in_tree + count, count)
                self.res[0] %= self.MOD
            nodes_in_tree += count
        return nodes_in_tree + 1
