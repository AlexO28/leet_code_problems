# construct binary tree from inorder and postorder traversal (all elements have different values)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTreeFromComponents(self, inorder, postorder):
        root_val = postorder[-1]
        ind = inorder.index(root_val)
        if ind == 0:
            tree_left = None
        else:
            inorder_left = inorder[:ind]
            postorder_left = postorder[:ind]
            tree_left = self.buildTreeFromComponents(inorder_left, postorder_left)
        if ind == len(inorder) - 1:
            tree_right = None
        else:
            inorder_right = inorder[(ind+1):]
            postorder_right = postorder[ind:(len(postorder)-1)]
            tree_right = self.buildTreeFromComponents(inorder_right, postorder_right)
        return TreeNode(root_val, tree_left, tree_right)

    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        return self.buildTreeFromComponents(inorder, postorder)
