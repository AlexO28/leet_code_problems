# You are given an undirected graph defined by an integer n, the number of nodes, and a 2D integer array edges, the edges in the graph, where edges[i] = [ui, vi] indicates that there is an undirected edge between ui and vi. You are also given an integer array queries.
# Let incident(a, b) be defined as the number of edges that are connected to either node a or b.
# The answer to the jth query is the number of pairs of nodes (a, b) that satisfy both of the following conditions:
# a < b
# incident(a, b) > queries[j]
# Return an array answers such that answers.length == queries.length and answers[j] is the answer of the jth query.
# Note that there can be multiple edges between the same two nodes.
from typing import List
from collections import defaultdict
from bisect import bisect_right


class Solution:
    def countPairs(
        self, n: int, edges: List[List[int]], queries: List[int]
    ) -> List[int]:
        cnt = [0] * n
        g = defaultdict(int)
        for a, b in edges:
            a -= 1
            b -= 1
            if a > b:
                a, b = b, a
            cnt[a] += 1
            cnt[b] += 1
            g[(a, b)] += 1
        s = sorted(cnt)
        ans = [0] * len(queries)
        for i, t in enumerate(queries):
            for j, x in enumerate(s):
                k = bisect_right(s, t - x, lo=j + 1)
                ans[i] += n - k
            for (a, b), v in g.items():
                if (cnt[a] + cnt[b] > t) and (cnt[a] + cnt[b] - v <= t):
                    ans[i] -= 1
        return ans
