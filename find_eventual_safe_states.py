# There is a directed graph of n nodes with each node labeled from 0 to n - 1. The graph is represented by a 0-indexed 2D integer array graph where graph[i] is an integer array of nodes adjacent to node i, meaning there is an edge from node i to each node in graph[i].
# A node is a terminal node if there are no outgoing edges. A node is a safe node if every possible path starting from that node leads to a terminal node (or another safe node).
# Return an array containing all the safe nodes of the graph. The answer should be sorted in ascending order.
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        self.graph = graph
        self.node_colors = [0]*(len(graph))
        return [ind for ind in range(len(graph)) if self.search(ind)]

    def search(self, ind):
        if self.node_colors[ind] > 0:
            return self.node_colors[ind] == 2
        else:
            self.node_colors[ind] = 1
            for next_ind in self.graph[ind]:
                if not self.search(next_ind):
                    return False
            self.node_colors[ind] = 2
            return True 
