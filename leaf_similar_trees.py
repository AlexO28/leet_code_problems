# Two binary trees are considered leaf-similar if their leaf value sequence is the same.
# Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaves1 = self.extractLeaves(root1)
        leaves2 = self.extractLeaves(root2)
        return leaves1 == leaves2

    def extractLeaves(self, tree):
        if tree is None:
            return []
        if (tree.left is None) and (tree.right is None):
            return [tree.val]
        left_res = self.extractLeaves(tree.left)
        right_res = self.extractLeaves(tree.right)
        left_res.extend(right_res)
        return left_res
