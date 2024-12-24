# Given the root of a binary tree, determine if it is a complete binary tree.
# In a complete binary tree, every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional
from collections import deque 


class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        nodes_queue = deque([root])
        while nodes_queue:
            current_node = nodes_queue.popleft()          
            if current_node is None:
                break          
            nodes_queue.append(current_node.left)
            nodes_queue.append(current_node.right)
        for node in nodes_queue:
            if node is not None:
                return False      
        return True
