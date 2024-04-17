# You are given the root of a binary tree where each node has a value in the range [0, 25] representing the letters 'a' to 'z'.
# Return the lexicographically smallest string that starts at a leaf of this tree and ends at the root.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return ""
        self.alphabet = "abcdefghijklmnopqrstuvwxyz"
        lines = self.extractLines(root)
        lines.sort()
        return lines[0]

    def extractLines(self, tree):
        if (tree.left is None) and (tree.right is None):
            return [self.alphabet[tree.val]]
        elif (tree.left is not None) and (tree.right is None):
            res_left = self.extractLines(tree.left)
            for j in range(len(res_left)):
                res_left[j] += self.alphabet[tree.val]
            return res_left
        elif (tree.left is None) and (tree.right is not None):
            res_right = self.extractLines(tree.right)
            for j in range(len(res_right)):
                res_right[j] += self.alphabet[tree.val]
            return res_right
        else:
            res_left = self.extractLines(tree.left)
            res_right = self.extractLines(tree.right)
            for j in range(len(res_left)):
                res_left[j] += self.alphabet[tree.val]
            for j in range(len(res_right)):
                res_right[j] += self.alphabet[tree.val]
            res_left.extend(res_right)
            return res_left
