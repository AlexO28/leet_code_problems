# Given an m x n matrix, return a new matrix answer where answer[row][col] is the rank of matrix[row][col].
# The rank is an integer that represents how large an element is compared to other elements. It is calculated using the following rules:
# The rank is an integer starting from 1.
# If two elements p and q are in the same row or column, then:
# If p < q then rank(p) < rank(q)
# If p == q then rank(p) == rank(q)
# If p > q then rank(p) > rank(q)
# The rank should be as small as possible.
# The test cases are generated so that answer is unique under the given rules.
from collections import defaultdict
from typing import List


class Solution:
    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        d = defaultdict(list)
        for i, row in enumerate(matrix):
            for j, v in enumerate(row):
                d[v].append((i, j))
        row_max = [0] * len(matrix)
        col_max = [0] * len(matrix[0])
        ans = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        uf = UnionFind(len(matrix) + len(matrix[0]))
        for v in sorted(d):
            rank = defaultdict(int)
            for i, j in d[v]:
                uf.union(i, j + len(matrix))
            for i, j in d[v]:
                rank[uf.find(i)] = max(rank[uf.find(i)], row_max[i], col_max[j])
            for i, j in d[v]:
                ans[i][j] = row_max[i] = col_max[j] = 1 + rank[uf.find(i)]
            for i, j in d[v]:
                uf.reset(i)
                uf.reset(j + len(matrix))
        return ans


class UnionFind:
    def __init__(self, n):
        self.p = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, a, b):
        pa, pb = self.find(a), self.find(b)
        if pa != pb:
            if self.size[pa] > self.size[pb]:
                self.p[pb] = pa
                self.size[pa] += self.size[pb]
            else:
                self.p[pa] = pb
                self.size[pb] += self.size[pa]

    def reset(self, x):
        self.p[x] = x
        self.size[x] = 1
