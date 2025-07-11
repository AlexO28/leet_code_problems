# Given two binary search trees root1 and root2, return a list containing all the integers from both trees sorted in ascending order.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional, List


class Solution:
    def getAllElements(
        self, root1: Optional[TreeNode], root2: Optional[TreeNode]
    ) -> List[int]:
        arr_1 = self.traverse(root1)
        arr_2 = self.traverse(root2)
        arr_1.extend(arr_2)
        arr_1.sort()
        return arr_1

    def traverse(self, tree):
        if tree is None:
            return [] 
        elif (tree.left is None) and (tree.right is None):
            return [tree.val]
        elif (tree.left is None) and (tree.right is not None):
            res = self.traverse(tree.right)
            res.append(tree.val)
            return list(set(res))
        elif (tree.left is not None) and (tree.right is None):
            res = self.traverse(tree.left)
            res.append(tree.val)
            return list(set(res))
        else:
            res_left = self.traverse(tree.left)
            res_right = self.traverse(tree.right)
            res = [tree.val]
            res.extend(res_left)
            res.extend(res_right)
            return list(set(res))
