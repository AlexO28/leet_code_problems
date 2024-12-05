# On a 2D plane, we place n stones at some integer coordinate points. Each coordinate point may have at most one stone.
# A stone can be removed if it shares either the same row or the same column as another stone that has not been removed.
# Given an array stones of length n where stones[i] = [xi, yi] represents the location of the ith stone, return the largest possible number of stones that can be removed.
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        num_nodes = 10001
        self.parent = list(range(num_nodes * 2))
        for x, y in stones:
            self.parent[self.find_root(x)] = self.find_root(y + num_nodes)
        unique_roots = {self.find_root(x) for x, y in stones}
        return len(stones) - len(unique_roots)

    def find_root(self, root_id):
        if self.parent[root_id] != root_id:
            self.parent[root_id] = self.find_root(self.parent[root_id])
        return self.parent[root_id]
