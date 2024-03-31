# Given the root node of a binary tree, your task is to create a string representation of the tree following a specific set of formatting rules. The representation should be based on a preorder traversal of the binary tree and must adhere to the following guidelines:
# Node Representation: Each node in the tree should be represented by its integer value.
# Parentheses for Children: If a node has at least one child (either left or right), its children should be represented inside parentheses. Specifically:
# If a node has a left child, the value of the left child should be enclosed in parentheses immediately following the node's value.
# If a node has a right child, the value of the right child should also be enclosed in parentheses. The parentheses for the right child should follow those of the left child.
# Omitting Empty Parentheses: Any empty parentheses pairs (i.e., ()) should be omitted from the final string representation of the tree, with one specific exception: when a node has a right child but no left child. In such cases, you must include an empty pair of parentheses to indicate the absence of the left child. This ensures that the one-to-one mapping between the string representation and the original binary tree structure is maintained.
# In summary, empty parentheses pairs should be omitted when a node has only a left child or no children. However, when a node has a right child but no left child, an empty pair of parentheses must precede the representation of the right child to reflect the tree's structure accurately.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        return self.serialise(root)

    def serialise(self, tree):
        res = str(tree.val)
        if tree.left is not None:
            left_kids = self.serialise(tree.left)
        else:
            left_kids = ""
        if tree.right is not None:
            right_kids = self.serialise(tree.right)
        else:
            right_kids = ""
        if (left_kids == "") and (right_kids != ""):
            res += "()(" + right_kids + ")"
        elif (left_kids != "") and (right_kids == ""):
            res += "(" + left_kids + ")"
        elif (left_kids != "") and (right_kids != ""):
            res += "(" + left_kids + ")(" + right_kids + ")"
        return res  
