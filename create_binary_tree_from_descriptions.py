# You are given a 2D integer array descriptions where descriptions[i] = [parenti, childi, isLefti] indicates that parenti is the parent of childi in a binary tree of unique values. Furthermore,
# If isLefti == 1, then childi is the left child of parenti.
# If isLefti == 0, then childi is the right child of parenti.
# Construct the binary tree described by descriptions and return its root.
# The test cases will be generated such that the binary tree is valid.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        self.descriptions_dict = {}
        children_nodes = []
        for description in descriptions:
            if description[0] in self.descriptions_dict:
                self.descriptions_dict[description[0]].append(description[1:])
            else:
                self.descriptions_dict[description[0]] = [description[1:]] 
            children_nodes.append(description[1])
        parent_node = [node for node in self.descriptions_dict if node not in children_nodes][0]
        return self.fillTreeByDict(parent_node)

    def fillTreeByDict(self, node):
        if node not in self.descriptions_dict:
            return TreeNode(node, None, None)
        else:
            left_kid = None
            right_kid = None
            for kid in self.descriptions_dict[node]:
                if kid[1] == 1:
                    left_kid = self.fillTreeByDict(kid[0])
                else:
                    right_kid = self.fillTreeByDict(kid[0])
            return TreeNode(node, left_kid, right_kid)
