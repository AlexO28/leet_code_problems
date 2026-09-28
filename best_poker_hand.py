# You are given an integer array ranks and a character array suits. You have 5 cards where the ith card has a rank of ranks[i] and a suit of suits[i].
# The following are the types of poker hands you can make from best to worst:
# "Flush": Five cards of the same suit.
# "Three of a Kind": Three cards of the same rank.
# "Pair": Two cards of the same rank.
# "High Card": Any single card.
# Return a string representing the best type of poker hand you can make with the given cards.
# Note that the return values are case-sensitive.
from collections import Counter


class Solution:
    def bestHand(self, ranks: list[int], suits: list[str]) -> str:
        if len(set(suits)) == 1:
            return "Flush"
        freqs = Counter(ranks)
        max_val = max(list(freqs.values()))
        if max_val >= 3:
            return "Three of a Kind"
        elif max_val == 2:
            return "Pair"
        else:
            return "High Card"
