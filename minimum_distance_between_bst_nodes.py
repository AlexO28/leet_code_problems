# Given the root of a Binary Search Tree (BST), return the minimum difference between the values of any two different nodes in the tree.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        nums = self.parseTree(root)
        nums.sort()
        return min([nums[i] - nums[i-1] for i in range(1, len(nums))])

    def parseTree(self, tree):
        if tree is None:
            return []
        res = [tree.val]
        res.extend(self.parseTree(tree.left))
        res.extend(self.parseTree(tree.right))
        return res
