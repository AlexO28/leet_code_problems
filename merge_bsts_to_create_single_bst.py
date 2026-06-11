# You are given n BST (binary search tree) root nodes for n separate BSTs stored in an array trees (0-indexed). Each BST in trees has at most 3 nodes, and no two roots have the same value. In one operation, you can:
# Select two distinct indices i and j such that the value stored at one of the leaves of trees[i] is equal to the root value of trees[j].
# Replace the leaf node in trees[i] with trees[j].
# Remove trees[j] from trees.
# Return the root of the resulting BST if it is possible to form a valid BST after performing n - 1 operations, or null if it is impossible to create a valid BST.
# A BST (binary search tree) is a binary tree where each node satisfies the following property:
# Every node in the node's left subtree has a value strictly less than the node's value.
# Every node in the node's right subtree has a value strictly greater than the node's value.
# A leaf is a node that has no children.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List, Optional


class Solution:
    def canMerge(self, trees: List[TreeNode]) -> Optional[TreeNode]:
        self.trees = {tree.val: tree for tree in trees}
        leaves = set()
        for tree in self.trees.values():
            if tree.left:
                if tree.left.val in leaves:
                    return None
                leaves.add(tree.left.val)
            if tree.right:
                if tree.right.val in leaves:
                    return None
                leaves.add(tree.right.val)
        candidates = {tree for tree in trees if tree.val not in leaves}
        if len(candidates) != 1:
            return None
        root_node = candidates.pop()
        self.trees.pop(root_node.val)
        root = root_node
        self.buildTree(root)
        if self.trees or not self.isValid(root)[0]:
            return None
        return root

    def buildTree(self, root: TreeNode) -> None:
        if root.left and root.left.val in self.trees:
            root.left = self.trees.pop(root.left.val)
            self.buildTree(root.left)
        if root.right and root.right.val in self.trees:
            root.right = self.trees.pop(root.right.val)
            self.buildTree(root.right)

    def isValid(self, root: TreeNode) -> (bool, int, int):
        minval = root.val
        maxval = root.val
        if root.left:
            leftvalid, leftmin, leftmax = self.isValid(root.left)
            if not leftvalid or leftmax >= root.val:
                return (False, minval, maxval)
            minval = leftmin
        if root.right:
            rightvalid, rightmin, rightmax = self.isValid(root.right)
            if not rightvalid or rightmin <= root.val:
                return (False, minval, maxval)
            maxval = rightmax
        return (True, minval, maxval)
