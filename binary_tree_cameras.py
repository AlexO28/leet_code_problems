# You are given the root of a binary tree. We install cameras on the tree nodes where each camera at a node can monitor its parent, itself, and its immediate children.
# Return the minimum number of cameras needed to monitor all nodes of the tree.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        self.limit_value = 1001
        min_camera_with_root, min_camera_with_parent, temp = self.search(root)
        return min(min_camera_with_root, min_camera_with_parent)


    def search(self, node):
        if node is None:
            return self.limit_value, 0, 0
        left_a, left_b, left_c = self.search(node.left)
        right_a, right_b, right_c = self.search(node.right)
        return min(left_a, left_b, left_c) + min(right_a, right_b, right_c) + 1, min(left_a + right_b, left_b + right_a, left_a + right_a), left_b + right_b
