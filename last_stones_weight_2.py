# You are given an array of integers stones where stones[i] is the weight of the ith stone.
# We are playing a game with the stones. On each turn, we choose any two stones and smash them together. Suppose the stones have weights x and y with x <= y. The result of this smash is:
# If x == y, both stones are destroyed, and
# If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
# At the end of the game, there is at most one stone left.
# Return the smallest possible weight of the left stone. If there are no stones left, return 0.#
from typing import List
from functools import cache


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        res = self.calculateStones(self.serialize(stones))
        return min([elem for elem in res if elem >= 0])

    
    @cache
    def calculateStones(self, stone_str):
        stones = [int(stone) for stone in stone_str.split(",")]
        if len(stones) == 1:
            return [stones[0]]
        elif len(stones) == 2:
            return list(set([stones[1] - stones[0], stones[0] - stones[1], stones[0] + stones[1], -stones[0]-stones[1]]))
        else:
            prev_res = self.calculateStones(self.serialize(stones[1:]))
            res = []
            for elem in prev_res:
                res.append(elem - stones[0])
                res.append(elem + stones[0])
                res.append(stones[0] - elem)
                res.append(-stones[0] - elem)
            return list(set(res))

    def serialize(self, stones):
        return ",".join(str(stone) for stone in stones)
