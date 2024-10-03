# Given the root of a binary tree, return the lowest common ancestor of its deepest leaves.
# Recall that:
# The node of a binary tree is a leaf if and only if it has no children
# The depth of the root of the tree is 0. if the depth of a node is d, the depth of each of its children is d + 1.
# The lowest common ancestor of a set S of nodes, is the node A with the largest depth such that every node in S is in the subtree with root A.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
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
        
