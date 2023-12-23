# Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing moving one unit north, south, east, or west, respectively. You start at the origin (0, 0) on a 2D plane and walk on the path specified by path.
# Return true if the path crosses itself at any point, that is, if at any time you are on a location you have previously visited. Return false otherwise.
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited = [[0, 0]]
        point = [0, 0]
        for elem in path:
            if elem == "N":
                point[1] += 1
            elif elem == "S":
                point[1] -= 1
            elif elem == "W":
                point[0] -= 1
            else:
                point[0] += 1
            if point in visited:
                return True
            else:
                visited.append(point.copy())
        return False
