# You are given a tree (i.e. a connected, undirected graph that has no cycles) consisting of n nodes numbered from 0 to n - 1 and exactly n - 1 edges. The root of the tree is the node 0, and each node of the tree has a label which is a lower-case character given in the string labels (i.e. The node with the number i has the label labels[i]).
# The edges array is given on the form edges[i] = [ai, bi], which means there is an edge between nodes ai and bi in the tree.
# Return an array of size n where ans[i] is the number of nodes in the subtree of the ith node which have the same label as node i.
# A subtree of a tree T is the tree consisting of a node in T and all of its descendant nodes.
from typing import List


class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        self.labels = list(labels)
        self.graph = {}
        for edge in edges:
            if edge[0] in self.graph:
                self.graph[edge[0]].append(edge[1])
            else:
                self.graph[edge[0]] = [edge[1]]
            if edge[1] in self.graph:
                self.graph[edge[1]].append(edge[0])
            else:
                self.graph[edge[1]] = [edge[0]]
        self.seen = set()
        self.visited = [0] * n
        self.traverse(0)
        return self.visited

    def traverse(self, index):
        self.seen.add(index)
        if index not in self.graph:
            self.visited[index] = 1
            return {self.labels[index]: 1}
        else:
            res_dict = {self.labels[index]: 1}
            for child in self.graph[index]:
                if child in self.seen:
                    continue
                child_dict = self.traverse(child)
                for elem in child_dict:
                    if elem in res_dict:
                        res_dict[elem] += child_dict[elem]
                    else:
                        res_dict[elem] = child_dict[elem]
            self.visited[index] = res_dict[self.labels[index]]
            return res_dict
