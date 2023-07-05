# Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. Each path should be returned as a list of the node values, not node references.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllPaths(self, tree):
        if (tree.left is None) and (tree.right is None):
            return [tree.val], [[tree.val]]
        if tree.left is None:
            heights, paths = self.getAllPaths(tree.right)
            heights = [tree.val + height for height in heights]
            for j in range(len(paths)):
                temp = [tree.val]
                temp.extend(paths[j])
                paths[j] = temp
            return heights, paths
        if tree.right is None:
            heights, paths = self.getAllPaths(tree.left)
            heights = [tree.val + height for height in heights]
            for j in range(len(paths)):
                temp = [tree.val]
                temp.extend(paths[j])
                paths[j] = temp
            return heights, paths
        heights, paths = self.getAllPaths(tree.left)
        heights_alt, paths_alt = self.getAllPaths(tree.right)
        heights.extend(heights_alt)
        paths.extend(paths_alt)
        heights = [tree.val + height for height in heights]
        for j in range(len(paths)):
            temp = [tree.val]
            temp.extend(paths[j])
            paths[j] = temp
        return heights, paths

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root is None:
            return []
        heights, paths = self.getAllPaths(root)
        res = []
        for j in range(len(heights)):
            if heights[j] == targetSum:
                res.append(paths[j])
        return res
