# You are given an integer array cards where cards[i] represents the value of the ith card. A pair of cards are matching if the cards have the same value.
# Return the minimum number of consecutive cards you have to pick up to have a pair of matching cards among the picked cards. If it is impossible to have matching cards, return -1.
from typing import List
from math import inf


class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        cards_dict = {}
        for j in range(len(cards)):
            if cards[j] in cards_dict:
                cards_dict[cards[j]].append(j)
            else:
                cards_dict[cards[j]] = [j]
        min_diff = inf
        for key in cards_dict:
            if len(cards_dict[key]) > 1:
                min_diff = min(min_diff, 1 + min([cards_dict[key][j + 1] - cards_dict[key][j] for j in range(len(cards_dict[key]) - 1)]))
        if min_diff < inf:
            return min_diff
        else:
            return -1
