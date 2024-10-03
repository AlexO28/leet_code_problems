# Given the root of a binary tree, the depth of each node is the shortest distance to the root.
# Return the smallest subtree such that it contains all the deepest nodes in the original tree.
# A node is called the deepest if it has the largest depth possible among any node in the entire tree.
# The subtree of a node is a tree consisting of that node, plus the set of all descendants of that node.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        depth, node = self.findMaxDepth(root)
        return node

    def findMaxDepth(self, tree):
        if (tree.left is None) and (tree.right is None):
            return 1, tree
        elif tree.left is None:
            depth_right, node_right = self.findMaxDepth(tree.right)
            return depth_right + 1, node_right
        elif tree.right is None:
            depth_left, node_left = self.findMaxDepth(tree.left)
            return depth_left + 1, node_left
        else:
            depth_left, node_left = self.findMaxDepth(tree.left)
            depth_right, node_right = self.findMaxDepth(tree.right)
            if depth_left == depth_right:
                return depth_left + 1, tree
            elif depth_left < depth_right:
                return depth_right + 1, node_right
            else:
                return depth_left + 1, node_left
