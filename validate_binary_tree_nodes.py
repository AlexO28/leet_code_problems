# You have n binary tree nodes numbered from 0 to n - 1 where node i has two children leftChild[i] and rightChild[i], return true if and only if all the given nodes form exactly one valid binary tree.
# If node i has no left child then leftChild[i] will equal -1, similarly for the right child.
# Note that the nodes have no values and that we only use the node numbers in this problem.
from typing import List


class Solution:
    def validateBinaryTreeNodes(
        self, n: int, leftChild: List[int], rightChild: List[int]
    ) -> bool:
        self.parents = list(range(n))
        visited = [False] * n
        for i, (left_child, right_child) in enumerate(zip(leftChild, rightChild)):
            for child in (left_child, right_child):
                if child != -1:
                    if visited[child] or self.find_root(i) == self.find_root(child):
                        return False
                    self.parents[self.find_root(i)] = self.find_root(child)
                    visited[child] = True
                    n -= 1
        return n == 1

    def find_root(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find_root(self.parents[x])
        return self.parents[x]
