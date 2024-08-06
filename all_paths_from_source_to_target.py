# Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1 and return them in any order.
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        cur_paths = [[0]]
        paths = []
        while len(cur_paths) > 0:
            new_paths = []
            for node_path in cur_paths:
                node = node_path[-1]
                if node == len(graph)-1:
                    paths.append(node_path.copy())
                else:
                    if len(graph[node]) > 0:
                        for neighbor in graph[node]:
                            temp = node_path.copy()
                            temp.append(neighbor)
                            new_paths.append(temp)
            cur_paths = new_paths
        return paths
