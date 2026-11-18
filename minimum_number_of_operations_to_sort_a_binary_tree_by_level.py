# You are given the root of a binary tree with unique values.
# In one operation, you can choose any two nodes at the same level and swap their values.
# Return the minimum number of operations needed to make the values at each level sorted in a strictly increasing order.
# The level of a node is the number of edges along the path between it and the root node.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def minimumOperations(self, root: TreeNode | None) -> int:
        q = deque([root])
        res = 0
        while q:
            t = []
            for _ in range(len(q)):
                node = q.popleft()
                t.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res += self._calculate(t)
        return res

    @staticmethod
    def _calculate(t):
        t_sorted = sorted(t)
        m = {v: i for i, v in enumerate(t_sorted)}
        for i in range(len(t)):
            t[i] = m[t[i]]
        res = 0
        for i in range(len(t)):
            while t[i] != i:
                Solution._swap(t, i, t[i])
                res += 1
        return res

    @staticmethod
    def _swap(arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]
