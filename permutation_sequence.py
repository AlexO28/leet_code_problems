# Given n and k, return the kth permutation sequence.


import itertools


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        init_values = list(range(1, n+1))
        permutations = list(itertools.permutations(init_values))
        perm_str = [str(s) for s in permutations[k-1]]
        return ''.join(perm_str)
