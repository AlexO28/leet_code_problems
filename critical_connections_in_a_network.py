# There are n servers numbered from 0 to n - 1 connected by undirected server-to-server connections forming a network where connections[i] = [ai, bi] represents a connection between servers ai and bi. Any server can reach other servers directly or indirectly through the network.
# A critical connection is a connection that, if removed, will make some servers unable to reach some other server.
# Return all critical connections in the network in any order.
from typing import List


class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        self.discovery_time = [0] * n
        self.low_time = [0] * n
        self.current_time = 0
        self.critical_connections = []
        self.graph = [set() for i in range(n)]
        for a, b in connections:
            self.graph[a].add(b)
            self.graph[b].add(a)
        self.search(0, -1)      
        return self.critical_connections


    def search(self, vertex, parent):
        self.current_time += 1
        self.discovery_time[vertex] = self.current_time
        self.low_time[vertex] = self.current_time
        for neighbor in self.graph[vertex]:
            if neighbor != parent:
                if not self.discovery_time[neighbor]:
                    self.search(neighbor, vertex)
                    self.low_time[vertex] = min(self.low_time[vertex], self.low_time[neighbor])
                    if self.low_time[neighbor] > self.discovery_time[vertex]:
                        self.critical_connections.append([vertex, neighbor])
                else:
                    self.low_time[vertex] = min(self.low_time[vertex], self.discovery_time[neighbor])
