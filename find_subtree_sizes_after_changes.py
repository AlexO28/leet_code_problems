# You are given a tree rooted at node 0 that consists of n nodes numbered from 0 to n - 1. The tree is represented by an array parent of size n, where parent[i] is the parent of node i. Since node 0 is the root, parent[0] == -1.
# You are also given a string s of length n, where s[i] is the character assigned to node i.
# We make the following changes on the tree one time simultaneously for all nodes x from 1 to n - 1:
# Find the closest node y to node x such that y is an ancestor of x, and s[x] == s[y].
# If node y does not exist, do nothing.
# Otherwise, remove the edge between x and its current parent and make node y the new parent of x by adding an edge between them.
# Return an array answer of size n where answer[i] is the size of the subtree rooted at node i in the final tree.
from typing import List


class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        g = [[] for _ in range(len(s))]
        for i in range(1, len(s)):
            g[parent[i]].append(i)
        d = [[] for _ in range(26)]
        res = [0] * len(s)
        stk = [(0, -1, 0)]
        while stk:
            i, fa, state = stk.pop()
            if state == 0:
                res[i] = 1
                idx = ord(s[i]) - 97
                d[idx].append(i)
                stk.append((i, fa, 1))
                for j in g[i]:
                    stk.append((j, i, 0))
            else:
                idx = ord(s[i]) - 97
                k = d[idx][-2] if len(d[idx]) > 1 else fa
                if k != -1:
                    res[k] += res[i]
                d[idx].pop()
        return res
