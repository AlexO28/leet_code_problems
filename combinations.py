# Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].
# You may return the answer in any order.


from itertools import combinations


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        comb_iter = combinations(list(range(1, n + 1)), k)
        for comb in comb_iter:
            res.append(comb)
        return res
