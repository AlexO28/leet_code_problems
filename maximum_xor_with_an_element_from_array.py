# You are given an array nums consisting of non-negative integers. You are also given a queries array, where queries[i] = [xi, mi].
# The answer to the ith query is the maximum bitwise XOR value of xi and any element of nums that does not exceed mi. In other words, the answer is max(nums[j] XOR xi) for all j such that nums[j] <= mi. If all elements in nums are larger than mi, then the answer is -1.
# Return an integer array answer where answer.length == queries.length and answer[i] is the answer to the ith query.
from typing import List


class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        trie = Trie()
        nums.sort()
        j = 0
        ans = [-1] * len(queries)
        for i, (x, m) in sorted(
            zip(range(len(queries)), queries), key=lambda x: x[1][1]
        ):
            while (j < len(nums)) and (nums[j] <= m):
                trie.insert(nums[j])
                j += 1
            ans[i] = trie.search(x)
        return ans


class Trie:
    __slots__ = ["children"]

    def __init__(self):
        self.children = [None] * 2

    def insert(self, x: int):
        node = self
        for i in range(30, -1, -1):
            v = x >> i & 1
            if node.children[v] is None:
                node.children[v] = Trie()
            node = node.children[v]

    def search(self, x: int) -> int:
        node = self
        ans = 0
        for i in range(30, -1, -1):
            v = x >> i & 1
            if node.children[v ^ 1]:
                ans |= 1 << i
                node = node.children[v ^ 1]
            elif node.children[v]:
                node = node.children[v]
            else:
                return -1
        return ans
