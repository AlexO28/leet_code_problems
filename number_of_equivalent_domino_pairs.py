# Given a list of dominoes, dominoes[i] = [a, b] is equivalent to dominoes[j] = [c, d] if and only if either (a == c and b == d), or (a == d and b == c) - that is, one domino can be rotated to be equal to another domino.
# Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length, and dominoes[i] is equivalent to dominoes[j].
from typing import List


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        freq_dict = {}
        for domino in dominoes:
            domino.sort()
            domino = tuple(domino)
            if domino in freq_dict:
                freq_dict[domino] += 1
            else:
                freq_dict[domino] = 1
        return int(sum((freq_dict[val] - 1)*freq_dict[val]/2 for val in freq_dict))
