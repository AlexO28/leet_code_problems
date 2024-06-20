# A virus is spreading rapidly, and your task is to quarantine the infected area by installing walls.
# The world is modeled as an m x n binary grid isInfected, where isInfected[i][j] == 0 represents uninfected cells, and isInfected[i][j] == 1 represents cells contaminated with the virus. A wall (and only one wall) can be installed between any two 4-directionally adjacent cells, on the shared boundary.
# Every night, the virus spreads to all neighboring cells in all four directions unless blocked by a wall. Resources are limited. Each day, you can install walls around only one region (i.e., the affected area (continuous block of infected cells) that threatens the most uninfected cells the following night). There will never be a tie.
# Return the number of walls used to quarantine all the infected regions. If the world will become fully infected, return the number of walls used.
class Solution:
    def containVirus(self, isInfected: List[List[int]]) -> int:
        self.isInfected = isInfected
        total_walls = 0
        while True:
            self.visited = [[False]*len(isInfected[0]) for i in range(len(isInfected))]
            self.areas = []
            self.walls_needed = []
            self.boundaries = []
            for i, row in enumerate(isInfected):
                for j, val in enumerate(row):
                    if val == 1 and not self.visited[i][j]:
                        self.areas.append([])
                        self.boundaries.append(set())
                        self.walls_needed.append(0)
                        self.dfs(i, j)
            if not self.areas:
                break
            index_most_boundaries = self.boundaries.index(max(self.boundaries, key=len))
            total_walls += self.walls_needed[index_most_boundaries]
            for k, area in enumerate(self.areas):
                if k == index_most_boundaries:
                    for i, j in area:
                        self.isInfected[i][j] = -1
                else:
                    for i, j in area:
                        for delta_x, delta_y in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                            x = i + delta_x
                            y = j + delta_y
                            if 0 <= x < len(isInfected) and 0 <= y < len(isInfected[0]) and self.isInfected[x][y] == 0:
                                self.isInfected[x][y] = 1
        return total_walls


    def dfs(self, i, j):
        self.visited[i][j] = True
        self.areas[-1].append((i, j))
        for delta_x, delta_y in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            x = i + delta_x
            y = j + delta_y
            if 0 <= x < len(self.isInfected) and 0 <= y < len(self.isInfected[0]):
                if self.isInfected[x][y] == 1 and not self.visited[x][y]:
                    self.dfs(x, y)
                elif self.isInfected[x][y] == 0:
                    self.walls_needed[-1] += 1
                    self.boundaries[-1].add((x, y))
