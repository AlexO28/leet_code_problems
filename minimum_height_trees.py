# A tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.
# Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges where edges[i] = [ai, bi] indicates that there is an undirected edge between the two nodes ai and bi in the tree, you can choose any node of the tree as the root. When you select a node x as the root, the result tree has height h. Among all possible rooted trees, those with minimum height (i.e. min(h))  are called minimum height trees (MHTs).
# Return a list of all MHTs' root labels. 


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        if n == 2:
            return [0, 1]
        leaves_dict = {}
        for edge in edges:
            if edge[0] in leaves_dict.keys():
                leaves_dict[edge[0]].append(edge[1])
            else:
                leaves_dict[edge[0]] = [edge[1]]
            if edge[1] in leaves_dict.keys():
                leaves_dict[edge[1]].append(edge[0])
            else:
                leaves_dict[edge[1]] = [edge[0]]
        leaves = []
        for vertix in leaves_dict.keys():
            if len(leaves_dict[vertix]) == 1:
                leaves.append(vertix)
        number_of_vertices = n
        number_of_vertices -= len(leaves)
        while (len(leaves) > 2) or (number_of_vertices > 0):
            new_leaves = []
            for leaf in leaves:
                vertix = leaves_dict.pop(leaf)
                vertix = vertix[0]
                leaves_dict[vertix].remove(leaf)
                if len(leaves_dict[vertix]) == 1:
                    new_leaves.append(vertix)
            leaves = new_leaves
            number_of_vertices -= len(leaves)
        return leaves
