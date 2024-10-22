# You are given the root of a binary tree and a positive integer k.
# The level sum in the tree is the sum of the values of the nodes that are on the same level.
# Return the kth largest level sum in the tree (not necessarily distinct). If there are fewer than k levels in the tree, return -1.
# Note that two nodes are on the same level if they have the same distance from the root.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        values = self.calculateAllLevels(root)
        if len(values) < k:
            return -1
        else:
            values.sort(reverse=True)
            return values[k-1]

    def calculateAllLevels(self, tree):
        if (tree.left is None) and (tree.right is None):
            return [tree.val]
        elif tree.left is None:
            res = [tree.val]
            res.extend(self.calculateAllLevels(tree.right))
            return res
        elif tree.right is None:
            res = [tree.val]
            res.extend(self.calculateAllLevels(tree.left))
            return res
        else:
            res = [tree.val]
            res_left = self.calculateAllLevels(tree.left)
            res_right = self.calculateAllLevels(tree.right)
            min_val = min(len(res_left), len(res_right))
            for i in range(min_val):
                res.append((res_left[i] + res_right[i]))
            if (len(res_right) == min_val) and (len(res_left) > min_val):
                i = min_val
                while i < len(res_left):
                    res.append(res_left[i])
                    i += 1
            elif (len(res_left) == min_val) and (len(res_right) > min_val):
                i = min_val
                while i < len(res_right):
                    res.append(res_right[i])
                    i += 1
            return res
