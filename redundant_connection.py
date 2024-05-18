# In this problem, a tree is an undirected graph that is connected and has no cycles.
# You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.
# Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        self.parents = list(range(len(edges) + 1))
        for a, b in edges:
            leader_a = self.find_set_leader(a)
            leader_b = self.find_set_leader(b)          
            if leader_a == leader_b:
                return [a, b]
            self.parents[leader_a] = leader_b      
        return []

    def find_set_leader(self, vertex):
        if self.parents[vertex] != vertex:
            self.parents[vertex] = self.find_set_leader(self.parents[vertex])
        return self.parents[vertex]
