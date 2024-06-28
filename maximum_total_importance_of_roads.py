# You are given an integer n denoting the number of cities in a country. The cities are numbered from 0 to n - 1.
# You are also given a 2D integer array roads where roads[i] = [ai, bi] denotes that there exists a bidirectional road connecting cities ai and bi.
# You need to assign each city with an integer value from 1 to n, where each value can only be used once. The importance of a road is then defined as the sum of the values of the two cities it connects.
# Return the maximum total importance of all roads possible after assigning the values optimally.
class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        road_dict = {}
        for start, end in roads:
            if start in road_dict:
                road_dict[start] += 1
            else:
                road_dict[start] = 1
            if end in road_dict:
                road_dict[end] += 1
            else:
                road_dict[end] = 1
        values = list(road_dict.values())
        values.sort(reverse=True)
        return sum([values[i]*(n-i) for i in range(len(values))])
