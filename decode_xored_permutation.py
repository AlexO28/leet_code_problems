# There is an integer array perm that is a permutation of the first n positive integers, where n is always odd.
# It was encoded into another integer array encoded of length n - 1, such that encoded[i] = perm[i] XOR perm[i + 1]. For example, if perm = [1,3,2], then encoded = [2,1].
# Given the encoded array, return the original array perm. It is guaranteed that the answer exists and is unique.
from typing import List


class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        x = 1
        for j in range(2, len(encoded) + 2):
            x ^= j
        res0 = x
        for j in range(1, len(encoded), 2):
            res0 ^= encoded[j]
        res = [res0]
        for j in range(1, len(encoded) + 1):
            res.append(res[-1] ^ encoded[j - 1])
        return res
