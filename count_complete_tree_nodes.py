# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def numberOfNodes(self, tree):
        num = 1
        if tree.left is not None:
            num += self.numberOfNodes(tree.left)
        if tree.right is not None:
            num += self.numberOfNodes(tree.right)
        return num

    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return self.numberOfNodes(root)
        
