# A complete binary tree is a binary tree in which every level, except possibly the last, is completely filled, and all nodes are as far left as possible.
# Design an algorithm to insert a new node to a complete binary tree keeping it complete after the insertion.
# Implement the CBTInserter class:
# CBTInserter(TreeNode root) Initializes the data structure with the root of the complete binary tree.
# int insert(int v) Inserts a TreeNode into the tree with value Node.val == val so that the tree remains complete, and returns the value of the parent of the inserted TreeNode.
# TreeNode get_root() Returns the root node of the tree.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class CBTInserter:

    def __init__(self, root: Optional[TreeNode]):
        self.tree_nodes = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            self.tree_nodes.append(node)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    def insert(self, val: int) -> int:
        parent_index = (len(self.tree_nodes) - 1) // 2
        new_node = TreeNode(val)
        self.tree_nodes.append(new_node)
        if self.tree_nodes[parent_index].left is None:
            self.tree_nodes[parent_index].left = new_node
        else:
            self.tree_nodes[parent_index].right = new_node
        return self.tree_nodes[parent_index].val

    def get_root(self) -> Optional[TreeNode]:
        return self.tree_nodes[0]

