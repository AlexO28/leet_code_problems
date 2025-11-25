# You are given the root of a binary tree and an integer distance. A pair of two different leaf nodes of a binary tree is said to be good if the length of the shortest path between them is less than or equal to distance.
# Return the number of good leaf node pairs in the tree.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import Counter
from typing import Optional


class Solution:
    def countPairs(self, root: Optional[TreeNode], distance: int) -> int:
        self.distance = distance
        if root is None:
            return 0
        pairs_count = self.countPairs(root.left, distance) + self.countPairs(
            root.right, distance
        )
        left_leaf_distances = Counter()
        right_leaf_distances = Counter()
        self.collect_leaf_distances(root.left, left_leaf_distances, 1)
        self.collect_leaf_distances(root.right, right_leaf_distances, 1)
        for left_distance, left_count in left_leaf_distances.items():
            for right_distance, right_count in right_leaf_distances.items():
                if left_distance + right_distance <= distance:
                    pairs_count += left_count * right_count
        return pairs_count

    def collect_leaf_distances(self, node, distance_counter, current_depth):
        if not (node is None or current_depth >= self.distance):
            if node.left is None and node.right is None:
                distance_counter[current_depth] += 1
            else:
                self.collect_leaf_distances(
                    node.left, distance_counter, current_depth + 1
                )
                self.collect_leaf_distances(
                    node.right, distance_counter, current_depth + 1
                )
