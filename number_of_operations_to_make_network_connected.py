# There are n computers numbered from 0 to n - 1 connected by ethernet cables connections forming a network where connections[i] = [ai, bi] represents a connection between computers ai and bi. Any computer can reach any other computer directly or indirectly through the network.
# You are given an initial computer network connections. You can extract certain cables between two directly connected computers, and place them between any pair of disconnected computers to make them directly connected.
# Return the minimum number of times you need to do this in order to make all the computers connected. If it is not possible, return -1.
from typing import List


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1
        number_of_components = 0
        vertices = [i for i in range(n)]
        self.connections_dict = {i: [] for i in range(n)}
        for a, b in connections:
            self.connections_dict[a].append(b)
            self.connections_dict[b].append(a)
        while len(vertices) > 0:
            number_of_components += 1
            new_vertices = set(self.find_component(vertices[0], set()))
            vertices = [vertex for vertex in vertices if vertex not in new_vertices]
        return number_of_components - 1

    def find_component(self, vertex, new_vertices):
        new_vertices.add(vertex)
        for element in self.connections_dict[vertex]:
            if element not in new_vertices:
                new_vertices.update(self.find_component(element, new_vertices))
        return new_vertices
