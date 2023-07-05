# Construct binary tree from inorder and preorder traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTreeFromComponents(self, preorder, inorder):
        ind = inorder.index(preorder[0])
        if ind == 0:
            tree_left = None
        else:
            inorder_left = inorder[:ind]
            preorder_left = preorder[1:(ind+1)]
            tree_left = self.buildTreeFromComponents(preorder_left, inorder_left)
        if ind == len(preorder) - 1:
            tree_right = None
        else:
            inorder_right = inorder[(ind+1):]
            preorder_right = preorder[(ind+1):]
            tree_right = self.buildTreeFromComponents(preorder_right, inorder_right)
        return TreeNode(preorder[0], tree_left, tree_right)

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        return self.buildTreeFromComponents(preorder, inorder)
