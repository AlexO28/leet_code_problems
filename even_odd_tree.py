# A binary tree is named Even-Odd if it meets the following conditions:
# The root of the binary tree is at level index 0, its children are at level index 1, their children are at level index 2, etc.
# For every even-indexed level, all nodes at the level have odd integer values in strictly increasing order (from left to right).
# For every odd-indexed level, all nodes at the level have even integer values in strictly decreasing order (from left to right).
# Given the root of a binary tree, return true if the binary tree is Even-Odd, otherwise return false.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        level = 0
        queue = deque([root])
        while queue:
            previous_value = 0 if level % 2 == 0 else float('inf')
            for _ in range(len(queue)):
                node = queue.popleft()
                if level % 2 == 0 and (node.val % 2 == 0 or previous_value >= node.val):
                    return False
                if level % 2 == 1 and (node.val % 2 == 1 or previous_value <= node.val):
                    return False
                previous_value = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level += 1
        return True
