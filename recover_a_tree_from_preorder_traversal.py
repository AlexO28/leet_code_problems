# We run a preorder depth-first search (DFS) on the root of a binary tree.
# At each node in this traversal, we output D dashes (where D is the depth of this node), then we output the value of this node.  If the depth of a node is D, the depth of its immediate child is D + 1.  The depth of the root node is 0.
# If a node has only one child, that child is guaranteed to be the left child.
# Given the output traversal of this traversal, recover the tree and return its root.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional


class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        nodes_stack = []
        current_depth = 0
        current_value = 0
        ord_0 = ord("0")
        for i in range(len(traversal)):
            if traversal[i] == "-":
                current_depth += 1
            else:
                current_value = 10 * current_value + (ord(traversal[i]) - ord_0)
            if (i+1 == len(traversal)) or (traversal[i].isdigit() and (traversal[i+1] == "-")):
                new_node = TreeNode(current_value)
                while len(nodes_stack) > current_depth:
                    nodes_stack.pop()
                if nodes_stack:
                    if nodes_stack[-1].left is None:
                        nodes_stack[-1].left = new_node
                    else:
                        nodes_stack[-1].right = new_node
                nodes_stack.append(new_node)
                current_depth = 0
                current_value = 0
        result = None
        while nodes_stack:
            result = nodes_stack.pop()
        return result
