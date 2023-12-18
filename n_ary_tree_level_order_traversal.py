# Given an n-ary tree, return the level order traversal of its nodes' values.
# Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None:
            return []
        return self.findLevelOrder(root)

    def findLevelOrder(self, tree):
        if len(tree.children) == 0:
            return [[tree.val]]
        res = [[tree.val]]
        struct = []
        max_len = 0
        for child in tree.children:
            temp = self.findLevelOrder(child)
            struct.append(temp)
            max_len = max(max_len, len(temp))
        for j in range(max_len):
            temp_arr = []
            for elem in struct:
                if len(elem) > j:
                    temp_arr.extend(elem[j])
            res.append(temp_arr)
        return res
