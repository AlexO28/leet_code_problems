# You are given an array pairs, where pairs[i] = [xi, yi], and:
# There are no duplicates.
# xi < yi
# Let ways be the number of rooted trees that satisfy the following conditions:
# The tree consists of nodes whose values appeared in pairs.
# A pair [xi, yi] exists in pairs if and only if xi is an ancestor of yi or yi is an ancestor of xi.
# Note: the tree does not have to be a binary tree.
# Two ways are considered to be different if there is at least one node that has different parents in both ways.
# Return:
# 0 if ways == 0
# 1 if ways == 1
# 2 if ways > 1
# A rooted tree is a tree that has a single root node, and all edges are oriented to be outgoing from the root.
# An ancestor of a node is any node on the path from the root to that node (excluding the node itself). The root has no ancestors.
from typing import List
from collections import defaultdict


class Solution:
    def checkWays(self, pairs: List[List[int]]) -> int:
        g = [[False] * 510 for _ in range(510)]
        v = defaultdict(list)
        for x, y in pairs:
            g[x][y] = True
            g[y][x] = True
            v[x].append(y)
            v[y].append(x)
        nodes = []
        for i in range(510):
            if v[i]:
                nodes.append(i)
                g[i][i] = True
        nodes.sort(key=lambda x: len(v[x]))
        equal = False
        root = 0
        for i, x in enumerate(nodes):
            j = i + 1
            while j < len(nodes) and not g[x][nodes[j]]:
                j += 1
            if j < len(nodes):
                y = nodes[j]
                if len(v[x]) == len(v[y]):
                    equal = True
                for z in v[x]:
                    if not g[y][z]:
                        return 0
            else:
                root += 1
        if root > 1:
            return 0
        if equal:
            return 2
        else:
            return 1
