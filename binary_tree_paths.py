# Given the root of a binary tree, return all root-to-leaf paths in any order.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        return self.extractPaths(root)

    def extractPaths(self, tree):
        if (tree.left is None) and (tree.right is None):
            return [str(tree.val)] 
        res = []
        if tree.left is not None:
            res_left = self.extractPaths(tree.left)
            for res_list in res_left:
                res_list = str(tree.val) + "->" + res_list
                res.append(res_list)
        if tree.right is not None:
            res_right = self.extractPaths(tree.right)
            for res_list in res_right:
                res_list = str(tree.val) + "->" + res_list
                res.append(res_list)
        return res
