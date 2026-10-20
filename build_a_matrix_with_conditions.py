# You are given a positive integer k. You are also given:
# a 2D integer array rowConditions of size n where rowConditions[i] = [abovei, belowi], and
# a 2D integer array colConditions of size m where colConditions[i] = [lefti, righti].
# The two arrays contain integers from 1 to k.
# You have to build a k x k matrix that contains each of the numbers from 1 to k exactly once. The remaining cells should have the value 0.
# The matrix should also satisfy the following conditions:
# The number abovei should appear in a row that is strictly above the row at which the number belowi appears for all i from 0 to n - 1.
# The number lefti should appear in a column that is strictly left of the column at which the number righti appears for all i from 0 to m - 1.
# Return any matrix that satisfies the conditions. If no answer exists, return an empty matrix.
from collections import defaultdict, deque


class Solution:
    def buildMatrix(self, k: int, rowConditions: list[list[int]], colConditions: list[list[int]]) -> list[list[int]]:
        row = self.search(rowConditions, k)
        col = self.search(colConditions, k)
        if row is None or col is None:
            return []
        res = [[0] * k for _ in range(k)]
        m = [0] * (k + 1)
        for i, v in enumerate(col):
            m[v] = i
        for i, v in enumerate(row):
            res[i][m[v]] = v
        return res
        
    def search(self, cond, k):
        g = defaultdict(list)
        indeg = [0] * (k + 1)
        for a, b in cond:
            g[a].append(b)
            indeg[b] += 1
        q = deque([i for i, v in enumerate(indeg[1:], 1) if v == 0])
        res = []
        while q:
            for _ in range(len(q)):
                i = q.popleft()
                res.append(i)
                for j in g[i]:
                    indeg[j] -= 1
                    if indeg[j] == 0:
                        q.append(j)
        return None if len(res) != k else res
