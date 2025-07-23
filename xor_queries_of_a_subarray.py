# You are given an array arr of positive integers. You are also given the array queries where queries[i] = [lefti, righti].
# For each query i compute the XOR of elements from lefti to righti (that is, arr[lefti] XOR arr[lefti + 1] XOR ... XOR arr[righti] ).
# Return an array answer where answer[i] is the answer to the ith query.
from typing import List
from itertools import accumulate
from operator import xor


class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        accumulated_xor = list(accumulate(arr, xor, initial=0))
        return [accumulated_xor[r + 1] ^ accumulated_xor[l] for l, r in queries]
