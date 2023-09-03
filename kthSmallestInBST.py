# Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, tree):
        arr = [tree.val]
        if tree.left is not None:
            arr.extend(self.getAllElements(tree.left))
        if tree.right is not None:
            arr.extend(self.getAllElements(tree.right))
        return arr

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        elements = self.getAllElements(root)
        elements.sort()
        return elements[k-1]
        
Console
