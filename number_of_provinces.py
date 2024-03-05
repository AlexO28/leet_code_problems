# There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.
# A province is a group of directly or indirectly connected cities and no other cities outside of the group.
# You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.
# Return the total number of provinces.
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        if len(isConnected) == 1:
            return 1
        number_of_provinces = 0
        visited = [False] * len(isConnected)
        for i in range(len(isConnected)):
            if not visited[i]:
                self.search(isConnected, visited, i)
                number_of_provinces += 1
        return number_of_provinces

    def search(self, isConnected, visited, i):
        for j in range(len(isConnected)):
            if (not visited[j]) and (isConnected[i][j] == 1):
                visited[j] = True
                self.search(isConnected, visited, j)
