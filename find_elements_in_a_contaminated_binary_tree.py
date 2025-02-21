# Given a binary tree with the following rules:
# root.val == 0
# For any treeNode:
# If treeNode.val has a value x and treeNode.left != null, then treeNode.left.val == 2 * x + 1
# If treeNode.val has a value x and treeNode.right != null, then treeNode.right.val == 2 * x + 2
# Now the binary tree is contaminated, which means all treeNode.val have been changed to -1.
# Implement the FindElements class:
# FindElements(TreeNode* root) Initializes the object with a contaminated binary tree and recovers it.
# bool find(int target) Returns true if the target value exists in the recovered binary tree.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.tree = root
        tree = self.tree
        tree.val = 0
        self.elements = {0: 1}
        self.fill(tree, 0)

    def fill(self, tree, level):
        if tree.left is not None:
            val_left = 2*level + 1
            tree.left.val = val_left
            self.elements[val_left] = 1
            self.fill(tree.left, val_left)
        if tree.right is not None:
            val_right = 2*level + 2
            tree.right.val = val_right
            self.elements[val_right] = 1
            self.fill(tree.right, val_right)


    def find(self, target: int) -> bool:
        return target in self.elements


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
