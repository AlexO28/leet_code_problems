# postorder traversal for binary tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTree(self, tree):
        res = []
        if tree.left is not None:
            res.extend(self.postorderTree(tree.left))
        if tree.right is not None:
            res.extend(self.postorderTree(tree.right))
        res.append(tree.val)
        return res

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        return self.postorderTree(root)
