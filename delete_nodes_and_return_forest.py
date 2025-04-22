# Given the root of a binary tree, each node in the tree has a distinct value.
# After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).
# Return the roots of the trees in the remaining forest. You may return the result in any order.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List, Optional


class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        self.to_delete = set(to_delete)
        self.forest = []
        if self.search(root) is not None:
            self.forest.append(root)
        return self.forest

    def search(self, tree):
        if tree is None:
            return None
        else:
            tree.left = self.search(tree.left)
            tree.right = self.search(tree.right)
            if tree.val in self.to_delete:
                if tree.left is not None:
                    self.forest.append(tree.left)
                if tree.right is not None:
                    self.forest.append(tree.right)
                return None
            else:
                return tree
