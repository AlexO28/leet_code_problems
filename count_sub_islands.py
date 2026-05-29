# You are given two m x n binary matrices grid1 and grid2 containing only 0's (representing water) and 1's (representing land). An island is a group of 1's connected 4-directionally (horizontal or vertical). Any cells outside of the grid are considered water cells.
# An island in grid2 is considered a sub-island if there is an island in grid1 that contains all the cells that make up this island in grid2.
# Return the number of islands in grid2 that are considered sub-islands.
from typing import List
import numpy as np
from scipy.ndimage import label


class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        grid2 = np.array(grid2)
        labeled_array, num_features = label(grid2)
        good_labels = {j: True for j in range(1, num_features + 1)}
        for i in range(len(labeled_array)):
            for j in range(len(labeled_array[0])):
                if labeled_array[i][j] > 0:
                    if grid1[i][j] == 0:
                        good_labels[labeled_array[i][j]] = False
        return len([label for label in good_labels if good_labels[label]])
