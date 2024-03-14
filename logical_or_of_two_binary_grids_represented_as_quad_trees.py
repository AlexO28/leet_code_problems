# A Binary Matrix is a matrix in which all the elements are either 0 or 1.
# Given quadTree1 and quadTree2. quadTree1 represents a n * n binary matrix and quadTree2 represents another n * n binary matrix.
# Return a Quad-Tree representing the n * n binary matrix which is the result of logical bitwise OR of the two binary matrixes represented by quadTree1 and quadTree2.
"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""
class Solution:
    def intersect(self, quadTree1: 'Node', quadTree2: 'Node') -> 'Node':
        if quadTree1 is None:
            return quadTree1
        else:
            return self.traverse_nodes(quadTree1, quadTree2)

    def traverse_nodes(self, node1, node2):
        if node1.isLeaf and node2.isLeaf:
            return Node(node1.val or node2.val, True, None, None, None, None)
        elif node1.isLeaf:
            if node1.val:
                return node1
            else:
                return node2
        elif node2.isLeaf:
            if node2.val:
                return node2
            else:
                return node1          
        else:
            result_node = Node(val=None, isLeaf=False, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None)
            result_node.topLeft = self.traverse_nodes(node1.topLeft, node2.topLeft)
            result_node.topRight = self.traverse_nodes(node1.topRight, node2.topRight)
            result_node.bottomLeft = self.traverse_nodes(node1.bottomLeft, node2.bottomLeft)
            result_node.bottomRight = self.traverse_nodes(node1.bottomRight, node2.bottomRight)
            all_children_are_leaves = result_node.topLeft.isLeaf and \
                                      result_node.topRight.isLeaf and \
                                      result_node.bottomLeft.isLeaf and \
                                      result_node.bottomRight.isLeaf
            if all_children_are_leaves and\
                (result_node.topLeft.val == result_node.topRight.val) and\
                (result_node.topLeft.val == result_node.bottomLeft.val) and\
                (result_node.topLeft.val == result_node.bottomRight.val):
                result_node = Node(result_node.topLeft.val, True, None, None, None, None)
            return result_node
