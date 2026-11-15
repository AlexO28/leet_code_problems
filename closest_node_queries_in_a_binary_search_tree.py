# You are given the root of a binary search tree and an array queries of size n consisting of positive integers.
# Find a 2D array answer of size n where answer[i] = [mini, maxi]:
# mini is the largest value in the tree that is smaller than or equal to queries[i]. If a such value does not exist, add -1 instead.
# maxi is the smallest value in the tree that is greater than or equal to queries[i]. If a such value does not exist, add -1 instead.
# Return the array answer.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from bisect import bisect_left, bisect_right


class Solution:
    def closestNodes(self, root: TreeNode | None, queries: list[int]) -> list[list[int]]:
        arr = []
        self._convertToArray(root, arr)
        arr.sort()
        res = []
        for query in queries:
            id_min = bisect_right(arr, query)
            if id_min > 0:
                val_min = arr[id_min - 1]
            else:
                val_min = -1
            id_max = bisect_left(arr, query)
            if id_max < len(arr):
                val_max = arr[id_max]
            else:
                val_max = -1
            res.append([val_min, val_max])
        return res

    def _convertToArray(self, root, arr):
        arr.append(root.val)
        if root.left is not None:
            self._convertToArray(root.left, arr)
        if root.right is not None:
            self._convertToArray(root.right, arr)
