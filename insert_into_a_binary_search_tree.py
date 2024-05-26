# You are given the root node of a binary search tree (BST) and a value to insert into the tree. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.
# Notice that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val, None, None)
        arr = self.BSTtoArray(root)
        arr.append(val)
        arr.sort(reverse=True)
        res = None
        for elem in arr:
            res = TreeNode(elem, None, res)
        return res

    def BSTtoArray(self, tree):
        if (tree.left is None) and (tree.right is None):
            return [tree.val]
        elif (tree.left is None):
            res = self.BSTtoArray(tree.right)
            res.append(tree.val)
            return res
        elif (tree.right is None):
            res = self.BSTtoArray(tree.left)
            res.append(tree.val)
            return res
        else:
            res_left = self.BSTtoArray(tree.left)
            res_right = self.BSTtoArray(tree.right)
            res_left.extend(res_right)
            res_left.append(tree.val)
            return res_left
