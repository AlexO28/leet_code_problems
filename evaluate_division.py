# You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.
# You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.
# Return the answers to all queries. If a single answer cannot be determined, return -1.0.
# Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.
# Note: The variables that do not occur in the list of equations are undefined, so the answer cannot be determined for them.
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = {}
        edges = {}
        for j in range(len(equations)):
            if equations[j][0] in graph:
                graph[equations[j][0]].append(equations[j][1])
            else:
                graph[equations[j][0]] = [equations[j][1]]
            if equations[j][1] in graph:
                graph[equations[j][1]].append(equations[j][0])
            else:
                graph[equations[j][1]] = [equations[j][0]]
            edges[equations[j][0] + "_" + equations[j][1]] = values[j]
            edges[equations[j][1] + "_" + equations[j][0]] = 1/values[j]
        res = []
        for query in queries:
            if query[0] not in graph.keys():
                res.append(-1)
                continue
            if query[1] not in graph.keys():
                res.append(-1)
                continue
            if query[1] == query[0]:
                res.append(1)
                continue
            visited = [query[0]]
            outputs = self.searchGraph(query[0], query[1], graph, edges, visited)
            if len(outputs) != 1:
                res.append(-1)
            else:
                res.append(outputs[0])                
        return res

    def searchGraph(self, source, destination, graph, edges, visited):
        for vertix in graph[source]:
            if vertix not in visited:
                if vertix == destination:
                    return [edges[source + "_" + destination]]
                else:
                    visited.append(vertix)
                    outputs = self.searchGraph(vertix, destination, graph, edges, visited)
                    if len(outputs) == 1:
                        return [edges[source + "_" + vertix] * outputs[0]]
        return []
