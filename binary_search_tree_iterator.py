# Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree (BST)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    def inorder_traversal(self, root):
        res = []
        if root.left is not None:
            res.extend(self.inorder_traversal(root.left))
        res.append(root.val)
        if root.right is not None:
            res.extend(self.inorder_traversal(root.right))
        return res


    def __init__(self, root: Optional[TreeNode]):
        self.arr = self.inorder_traversal(root)
        self.pos = 0

    def next(self) -> int:
        self.pos += 1
        return self.arr[self.pos-1]
        
    def hasNext(self) -> bool:
        return self.pos < len(self.arr)

