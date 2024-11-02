# You are given an integer array deck where deck[i] represents the number written on the ith card.
# Partition the cards into one or more groups such that:
# Each group has exactly x cards where x > 1, and
# All the cards in one group have the same integer written on them.
# Return true if such partition is possible, or false otherwise.
import math


class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        groups = {}
        for card in deck:
            if card in groups:
                groups[card] += 1
            else:
                groups[card] = 1
        return math.gcd(*list(groups.values())) > 1
