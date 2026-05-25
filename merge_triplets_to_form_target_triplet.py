# A triplet is an array of three integers. You are given a 2D integer array triplets, where triplets[i] = [ai, bi, ci] describes the ith triplet. You are also given an integer array target = [x, y, z] that describes the triplet you want to obtain.
# To obtain target, you may apply the following operation on triplets any number of times (possibly zero):
# Choose two indices (0-indexed) i and j (i != j) and update triplets[j] to become [max(ai, aj), max(bi, bj), max(ci, cj)].
# For example, if triplets[i] = [2, 5, 3] and triplets[j] = [1, 7, 5], triplets[j] will be updated to [max(2, 1), max(5, 7), max(3, 5)] = [2, 7, 5].
# Return true if it is possible to obtain the target triplet [x, y, z] as an element of triplets, or false otherwise.
from typing import List


class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        x = 0
        y = 0
        z = 0
        for triplet in triplets:
            if (
                (triplet[0] <= target[0])
                and (triplet[1] <= target[1])
                and (triplet[2] <= target[2])
            ):
                x = max(x, triplet[0])
                y = max(y, triplet[1])
                z = max(z, triplet[2])
        return (x == target[0]) and (y == target[1]) and (z == target[2])
