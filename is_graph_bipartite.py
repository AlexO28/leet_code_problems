# There is an undirected graph with n nodes, where each node is numbered between 0 and n - 1. You are given a 2D array graph, where graph[u] is an array of nodes that node u is adjacent to. More formally, for each v in graph[u], there is an undirected edge between node u and node v. The graph has the following properties:
# There are no self-edges (graph[u] does not contain u).
# There are no parallel edges (graph[u] does not contain duplicate values).
# If v is in graph[u], then u is in graph[v] (the graph is undirected).
# The graph may not be connected, meaning there may be two nodes u and v such that there is no path between them.
# A graph is bipartite if the nodes can be partitioned into two independent sets A and B such that every edge in the graph connects a node in set A and a node in set B.
# Return true if and only if it is bipartite.
import queue


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        if len(graph) == 1:
            return True
        part_1 = []
        part_2 = []
        q = queue.Queue()
        indices = [i for i in range(len(graph))]
        while True:
            if q.qsize() == 0:
                if len(indices) == 0:
                    return (len(part_1) > 0) and (len(part_2) > 0)
                elem = indices.pop(0)
                q.put([elem, True])
            else:
                elem, put_into_part_1 = q.get()
                if put_into_part_1:
                    part_1.append(elem)
                    part_1 = list(set(part_1))
                else:
                    part_2.append(elem)
                    part_2 = list(set(part_2))
                kids = graph[elem]
                for kid in kids:
                    if put_into_part_1:
                        if kid in part_1:
                            return False
                        part_2.append(kid)
                        part_2 = list(set(part_2))
                    else:
                        if kid in part_2:
                            return False
                        part_1.append(kid)
                        part_1 = list(set(part_1))
                    if kid in indices:
                        q.put([kid, not put_into_part_1])
                        indices.remove(kid)
