# In an infinite binary tree where every node has two children, the nodes are labelled in row order.
# In the odd numbered rows (ie., the first, third, fifth,...), the labelling is left to right, while in the even numbered rows (second, fourth, sixth,...), the labelling is right to left.
# Given the label of a node in this tree, return the labels in the path from the root of the tree to the node with that label.
from typing import List


class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        level_start_value = 1
        level_index = 1
        level_next = 2 * level_start_value
        while level_next <= label:
            level_start_value = level_next
            level_index += 1
            level_next *= 2
        path = [0] * level_index
        while level_index > 0:
            path[level_index - 1] = label
            label = ((1 << (level_index - 1)) + (1 << level_index) - 1 - label) >> 1
            level_index -= 1
        return path
