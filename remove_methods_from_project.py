# You are maintaining a project that has n methods numbered from 0 to n - 1.
# You are given two integers n and k, and a 2D integer array invocations, where invocations[i] = [ai, bi] indicates that method ai invokes method bi.
# There is a known bug in method k. Method k, along with any method invoked by it, either directly or indirectly, are considered suspicious and we aim to remove them.
# A group of methods can only be removed if no method outside the group invokes any methods within it.
# Return an array containing all the remaining methods after removing all the suspicious methods. You may return the answer in any order. If it is not possible to remove all the suspicious methods, none should be removed.
from typing import List


class Solution:
    def remainingMethods(
        self, n: int, k: int, invocations: List[List[int]]
    ) -> List[int]:
        self.nodes = {}
        for a, b in invocations:
            if a in self.nodes:
                self.nodes[a].append(b)
            else:
                self.nodes[a] = [b]
        self.suspicous = set()
        self.search(k)
        found = False
        for elem in self.nodes:
            if elem not in self.suspicous:
                for child in self.nodes[elem]:
                    if child in self.suspicous:
                        found = True
                        break
        if found:
            return [elem for elem in range(n)]
        else:
            return [
                elem
                for elem in range(n)
                if elem not in self.suspicous
            ]

    def search(self, x):
        self.suspicous.add(x)
        if x in self.nodes:
            for child in self.nodes[x]:
                if child not in self.suspicous:
                    self.search(child)
