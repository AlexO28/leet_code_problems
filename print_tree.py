# Given the root of a binary tree, construct a 0-indexed m x n string matrix res that represents a formatted layout of the tree. The formatted layout matrix should be constructed using the following rules:
# The height of the tree is height and the number of rows m should be equal to height + 1.
# The number of columns n should be equal to 2height+1 - 1.
# Place the root node in the middle of the top row (more formally, at location res[0][(n-1)/2]).
# For each node that has been placed in the matrix at position res[r][c], place its left child at res[r+1][c-2height-r-1] and its right child at res[r+1][c+2height-r-1].
# Continue this process until all the nodes in the tree have been placed.
# Any empty cells should contain the empty string "".
# Return the constructed matrix res.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        m = self.maxHeight(root)
        n = pow(2, m) - 1
        self.res = [[''] * n for i in range(m)]
        self.dfs(root, 0, 0, len(self.res[0]) - 1)
        return self.res

    def maxHeight(self, root):
        if root is None:
            return 0
        else:
            return 1 + max(self.maxHeight(root.left), self.maxHeight(root.right))

    def dfs(self, root, row, left, right):
        if root is None:
            return None
        mid = (left + right) // 2
        self.res[row][mid] = str(root.val)
        self.dfs(root.left, row + 1, left, mid - 1)
        self.dfs(root.right, row + 1, mid + 1, right)
