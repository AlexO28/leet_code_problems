# Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.
# Return the number of good nodes in the binary tree.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.search(root, root.val)

    def search(self, tree, cur_max):
        if tree.val > cur_max:
            cur_max = tree.val
            res = 1
        elif tree.val == cur_max:
            res = 1
        else:
            res = 0
        if tree.left is not None:
            res_left = self.search(tree.left, cur_max)
        else:
            res_left = 0
        if tree.right is not None:
            res_right = self.search(tree.right, cur_max)
        else:
            res_right = 0
        return res + res_left + res_right
