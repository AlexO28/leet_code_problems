from scipy.spatial import ConvexHull

class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        try:
            hull = ConvexHull(trees)
        except:
            return trees
        res = [trees[hull.vertices[0]]]
        for j in range(1, len(hull.vertices)+1):
            prev_ind = j-1
            if j == len(hull.vertices):
                j = 0
            else:
                res.append(trees[hull.vertices[j]])
            dist = (abs(trees[hull.vertices[j]][0] - trees[hull.vertices[j-1]][0]) ** 2 + abs(trees[hull.vertices[j]][1] - trees[hull.vertices[j-1]][1]) ** 2) ** 0.5
            for point in trees:
                if point not in res:
                    dist1 = (abs(point[0] - trees[hull.vertices[j-1]][0]) ** 2 + abs(point[1] - trees[hull.vertices[j-1]][1]) ** 2) ** 0.5
                    dist2 = (abs(trees[hull.vertices[j]][0] - point[0]) ** 2 + abs(trees[hull.vertices[j]][1] - point[1]) ** 2) ** 0.5
                    if abs(dist1 + dist2 - dist) <= 0.0001 and (dist1 > 0) and (dist2 > 0):
                        res.append(point)
        return res
  
