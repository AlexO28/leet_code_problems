# You are given a 0-indexed m x n binary matrix land where a 0 represents a hectare of forested land and a 1 represents a hectare of farmland.
# To keep the land organized, there are designated rectangular areas of hectares that consist entirely of farmland. These rectangular areas are called groups. No two groups are adjacent, meaning farmland in one group is not four-directionally adjacent to another farmland in a different group.
# land can be represented by a coordinate system where the top left corner of land is (0, 0) and the bottom right corner of land is (m-1, n-1). Find the coordinates of the top left and bottom right corner of each group of farmland. A group of farmland with a top left corner at (r1, c1) and a bottom right corner at (r2, c2) is represented by the 4-length array [r1, c1, r2, c2].
# Return a 2D array containing the 4-length arrays described above for each group of farmland in land. If there are no groups of farmland, return an empty array. You may return the answer in any order.
import numpy as np
from typing import List
from scipy.ndimage import label


class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        land = np.array(land)
        structure = [[0, 1, 0], [1, 1, 1], [0, 1, 0]]
        labels, num_features = label(land, structure=structure)
        res = [[len(land), len(land[0]), -1, -1] for elem in range(num_features)]
        for i in range(len(labels)):
            for j in range(len(labels[0])):
                if labels[i][j] > 0:
                    vec = res[labels[i][j] - 1]
                    vec[0] = min(vec[0], i)
                    vec[1] = min(vec[1], j)
                    vec[2] = max(vec[2], i)
                    vec[3] = max(vec[3], j)
                    res[labels[i][j] - 1] = vec
        return res
