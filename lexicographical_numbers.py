# Given an integer n, return all the numbers in the range [1, n] sorted in lexicographical order.

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = [str(i) for i in range(1, n+1)]
        res.sort()
        return [int(r) for r in res]
