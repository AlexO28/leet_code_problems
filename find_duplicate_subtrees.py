# Given the root of a binary tree, return all duplicate subtrees.
# For each kind of duplicate subtrees, you only need to return the root node of any one of them.
# Two trees are duplicate if they have the same structure with the same node values.
from collections import Counter


class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        self.duplicate_subtrees = []
        self.subtree_counter = Counter()
        self.traverse(root)
        return self.duplicate_subtrees

    def traverse(self, node):
        if node is None:
            return "#"
        serialized_subtree = "{" + str(node.val) + "}" + "," + "{" + self.traverse(node.left) + "}" + "," + "{" + self.traverse(node.right) + "}"
        self.subtree_counter[serialized_subtree] += 1
        if self.subtree_counter[serialized_subtree] == 2:
            self.duplicate_subtrees.append(node)
        return serialized_subtree
