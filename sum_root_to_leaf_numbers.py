# You are given the root of a binary tree containing digits from 0 to 9 only.
# Each root-to-leaf path in the tree represents a number.
# For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
# Return the total sum of all root-to-leaf numbers.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def extractPathsForTree(self, tree):
        if (tree.left is None) and (tree.right is None):
            return [str(tree.val)]
        if (tree.left is not None) and (tree.right is not None):
            leftPaths = self.extractPathsForTree(tree.left)
            rightPaths = self.extractPathsForTree(tree.right)
            new_paths = []
            for path in leftPaths:
                new_paths.append(str(tree.val) + path)
            for path in rightPaths:
                new_paths.append(str(tree.val) + path)
            return new_paths
        if tree.left is None:
            rightPaths = self.extractPathsForTree(tree.right)
            new_paths = []
            for path in rightPaths:
                new_paths.append(str(tree.val) + path)
            return new_paths
        leftPaths = self.extractPathsForTree(tree.left)
        new_paths = []
        for path in leftPaths:
            new_paths.append(str(tree.val) + path)
        return new_paths

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        paths = self.extractPathsForTree(root)
        num = 0
        for path in paths:
            num += int(path)
        return num
