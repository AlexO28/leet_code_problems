# You are given the root of a binary tree with n nodes, where each node is uniquely assigned a value from 1 to n. You are also given a sequence of n values voyage, which is the desired pre-order traversal of the binary tree.
# Any node in the binary tree can be flipped by swapping its left and right subtrees. For example, flipping node 1 will have the following effect:
# Flip the smallest number of nodes so that the pre-order traversal of the tree matches voyage.
# Return a list of the values of all flipped nodes. You may return the answer in any order. If it is impossible to flip the nodes in the tree to make the pre-order traversal match voyage, return the list [-1].
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List


class Solution:
    def flipMatchVoyage(self, root: Optional[TreeNode], voyage: List[int]) -> List[int]:
        res = []
        i = 0
        stack = []
        stack.append(root)
        while len(stack) > 0:
            node = stack.pop()
            if node is not None:
                if node.val != voyage[i]:
                    return [-1]
                else:
                    i += 1
                if (node.right is not None) and (node.right.val == voyage[i]):
                    if node.left is not None:
                        res.append(node.val)
                    stack.append(node.left)
                    stack.append(node.right)
                else:
                    stack.append(node.right)
                    stack.append(node.left)
        return res
