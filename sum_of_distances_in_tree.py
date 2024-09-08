# There is an undirected connected tree with n nodes labeled from 0 to n - 1 and n - 1 edges.
# You are given the integer n and the array edges where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree.
# Return an array answer of length n where answer[i] is the sum of the distances between the ith node in the tree and all other nodes.
class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        self.neighbors = {}
        for edge in edges:
            if edge[0] in self.neighbors:
                self.neighbors[edge[0]].append(edge[1])
            else:
                self.neighbors[edge[0]] = [edge[1]]
            if edge[1] in self.neighbors:
                self.neighbors[edge[1]].append(edge[0])
            else:
                self.neighbors[edge[1]] = [edge[0]]
        self.total_distance = [0]
        self.subtree_size = [0]*n
        self.distances = [0]*n
        self.n = n
        self.calculate_distance_and_size(0, -1, 0)
        self.search_for_new_root(0, -1, self.total_distance[0])
        return self.distances

    def calculate_distance_and_size(self, current, parent, depth):
        self.total_distance[0] += depth
        self.subtree_size[current] = 1
        if current in self.neighbors:
            for neighbor in self.neighbors[current]:
                if neighbor != parent:
                    self.calculate_distance_and_size(neighbor, current, depth+1)
                    self.subtree_size[current] += self.subtree_size[neighbor]

    def search_for_new_root(self, current, parent, total_distance):
        self.distances[current] = total_distance
        if current in self.neighbors:
            for neighbor in self.neighbors[current]:
                if neighbor != parent:
                    self.search_for_new_root(neighbor, current, total_distance-2*self.subtree_size[neighbor]+self.n)
