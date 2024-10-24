# Given two integer arrays, preorder and postorder where preorder is the preorder traversal of a binary tree of distinct values and postorder is the postorder traversal of the same tree, reconstruct and return the binary tree.
# If there exist multiple answers, you can return any of them.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        return self.construct(preorder, postorder)


    def construct(self, preorder, postorder):
        if len(preorder) == 0:
            return None
        tree = TreeNode(preorder[0])
        if len(preorder) == 1:
            return tree
        for i in range(len(preorder)-1):
            if postorder[i] == preorder[1]:
                tree.left = self.construct(preorder[1:(i+2)], postorder[:(i+1)])
                tree.right = self.construct(preorder[(i+2):], postorder[(i+1):(-1)])
                return tree
