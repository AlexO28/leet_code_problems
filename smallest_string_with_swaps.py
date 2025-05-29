# You are given a string s, and an array of pairs of indices in the string pairs where pairs[i] = [a, b] indicates 2 indices(0-indexed) of the string.
# You can swap the characters at any pair of indices in the given pairs any number of times.
# Return the lexicographically smallest string that s can be changed to after using the swaps.
from typing import List
from collections import defaultdict


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        self.parent = list(range(len(s)))
        for a, b in pairs:
            self.parent[self.find_root(a)] = self.find_root(b)
        char_group = defaultdict(list)
        for i, c in enumerate(s):
            char_group[self.find_root(i)].append(c)
        for chars in char_group.values():
            chars.sort(reverse=True)
        output = "".join(char_group[self.find_root(i)].pop() for i in range(len(s)))
        return output


    def find_root(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find_root(self.parent[x])
        return self.parent[x]
