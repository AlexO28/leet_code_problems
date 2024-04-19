# You are given an integer array nums with no duplicates. A maximum binary tree can be built recursively from nums using the following algorithm:
# Create a root node whose value is the maximum value in nums.
# Recursively build the left subtree on the subarray prefix to the left of the maximum value.
# Recursively build the right subtree on the subarray suffix to the right of the maximum value.
# Return the maximum binary tree built from nums.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        return self.recursivelyBuild(nums)

    def recursivelyBuild(self, nums):
        if len(nums) == 1:
            return TreeNode(nums[0], None, None)
        max_val = -1
        ind = -1
        for j in range(len(nums)):
            if nums[j] > max_val:
                max_val = nums[j]
                ind = j
        if ind == 0:
            right_tree = self.recursivelyBuild(nums[(ind+1):])
            return TreeNode(nums[0], None, right_tree)
        elif ind == len(nums)-1:
            left_tree = self.recursivelyBuild(nums[:ind])
            return TreeNode(nums[-1], left_tree, None)
        else:
            left_tree = self.recursivelyBuild(nums[:ind])
            right_tree = self.recursivelyBuild(nums[(ind+1):])
            return TreeNode(nums[ind], left_tree, right_tree)
