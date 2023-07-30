# preorder traversal for the binary tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTree(self, tree):
        res = [tree.val]
        if tree.left is not None:
            res.extend(self.preorderTree(tree.left))
        if tree.right is not None:
            res.extend(self.preorderTree(tree.right))
        return res

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        return self.preorderTree(root)
