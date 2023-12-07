# Your task is to calculate ab mod 1337 where a is a positive integer and b is an extremely large positive integer given in the form of an array.
class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        res = 1
        for j in range(len(b) - 1, -1, -1):
            res = (res * (a ** b[j])) % 1337
            a = (a ** 10) % 1337
        return res
