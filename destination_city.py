# You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct path going from cityAi to cityBi. Return the destination city, that is, the city without any path outgoing to another city.
# It is guaranteed that the graph of paths forms a line without any loop, therefore, there will be exactly one destination city.
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        if len(paths) == 1:
            return paths[0][1]
        left_vertices = []
        right_vertices = []
        for path in paths:
            if path[0] not in left_vertices:
                left_vertices.append(path[0])
            if path[0] in right_vertices:
                right_vertices.remove(path[0])
            if path[1] in left_vertices:
                if path[1] in right_vertices:
                    right_vertices.remove(path[1])
            else:
                right_vertices.append(path[1])
        return right_vertices[0]
