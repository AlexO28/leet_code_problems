# You are given the root of a binary search tree (BST) and an integer val.
# Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        self.val = val
        return self.search(root)

    def search(self, tree):
        if tree.val == self.val:
            return tree
        else:
            if (tree.left is None) and (tree.right is None):
                return None
            if tree.val > self.val:
                if tree.left is None:
                    return None
                else:
                    return self.search(tree.left)
            else:
                if tree.right is None:
                    return None
                else:
                    return self.search(tree.right)
 
