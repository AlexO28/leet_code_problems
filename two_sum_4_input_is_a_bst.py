# Given the root of a binary search tree and an integer k, return true if there exist two elements in the BST such that their sum is equal to k, or false otherwise.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        self.freq_dict = {}
        self.parseTree(root)
        for key in self.freq_dict:
            if key != k - key:
                if k - key in self.freq_dict:
                    return True
            else:
                if self.freq_dict[key] > 1:
                    return True
        return False

    def parseTree(self, tree):
        if tree.val in self.freq_dict:
            self.freq_dict[tree.val] = 2
        else:
            self.freq_dict[tree.val] = 1
        if tree.left is not None:
            self.parseTree(tree.left)
        if tree.right is not None:
            self.parseTree(tree.right)
