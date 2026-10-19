# You are given the root of a binary tree with unique values, and an integer start. At minute 0, an infection starts from the node with value start.
# Each minute, a node becomes infected if:
# The node is currently uninfected.
# The node is adjacent to an infected node.
# Return the number of minutes needed for the entire tree to be infected.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict


class Solution:
    def amountOfTime(self, root: TreeNode | None, start: int) -> int:
        g = defaultdict(list)
        stk = [(root, None)]
        while stk:
            node, fa = stk.pop()
            if node is not None:
                if fa:
                    g[node.val].append(fa.val)
                    g[fa.val].append(node.val)
                stk.append((node.right, node))
                stk.append((node.left, node))
        dist = {}
        walk = [(start, -1, 0)]
        while walk:
            node, fa, state = walk.pop()
            nxts = g[node]
            if state == 0:
                walk.append((node, fa, 1))
                for nxt in reversed(nxts):
                    if nxt != fa:
                        walk.append((nxt, node, 0))
            else:
                best = 0
                for nxt in nxts:
                    if nxt != fa:
                        best = max(best, 1 + dist[nxt])
                dist[node] = best
        return dist[start]
