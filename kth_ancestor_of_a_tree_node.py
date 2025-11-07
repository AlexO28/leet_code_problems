# You are given a tree with n nodes numbered from 0 to n - 1 in the form of a parent array parent where parent[i] is the parent of ith node. The root of the tree is node 0. Find the kth ancestor of a given node.
# The kth ancestor of a tree node is the kth node in the path from that node to the root node.
# Implement the TreeAncestor class:
# TreeAncestor(int n, int[] parent) Initializes the object with the number of nodes in the tree and the parent array.
# int getKthAncestor(int node, int k) return the kth ancestor of the given node node. If there is no such ancestor, return -1.
from typing import List


class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        max_power = 18
        self.ancestors = [[-1] * max_power for i in range(n)]
        for node, parent_node in enumerate(parent):
            self.ancestors[node][0] = parent_node
        for power in range(1, max_power):
            for node in range(n):
                if self.ancestors[node][power - 1] == -1:
                    continue
                intermediate_ancestor = self.ancestors[node][power - 1]
                self.ancestors[node][power] = self.ancestors[intermediate_ancestor][
                    power - 1
                ]

    def getKthAncestor(self, node: int, k: int) -> int:
        for bit_position in range(17, -1, -1):
            if (k >> bit_position) & 1:
                node = self.ancestors[node][bit_position]
                if node == -1:
                    break
        return node
