# A peak element in a 2D grid is an element that is strictly greater than all of its adjacent neighbors to the left, right, top, and bottom.
# Given a 0-indexed m x n matrix mat where no two adjacent cells are equal, find any peak element mat[i][j] and return the length 2 array [i,j].
# You may assume that the entire matrix is surrounded by an outer perimeter with the value -1 in each cell.
# You must write an algorithm that runs in O(m log(n)) or O(n log(m)) time.
from typing import List


class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        self.mat = mat
        indexes_from_rows = len(mat) >= len(mat[0])
        if indexes_from_rows:
            return self.search(0, len(mat) - 1, True)
        else:
            return self.search(0, len(mat[0]) - 1, False)[::-1]

    def search(self, start, end, indexes_from_rows):
        if end == start:
            return start, self.which_max(start, indexes_from_rows)
        elif end - start == 1:
            if self.find_max(start, indexes_from_rows) > self.find_max(
                end, indexes_from_rows
            ):
                return start, self.which_max(start, indexes_from_rows)
            else:
                return end, self.which_max(end, indexes_from_rows)
        else:
            middle = (end + start) // 2
            left = middle - 1
            right = middle + 1
            middle_max = self.find_max(middle, indexes_from_rows)
            left_max = self.find_max(left, indexes_from_rows)
            right_max = self.find_max(right, indexes_from_rows)
            if (middle_max > left_max) and (middle_max > right_max):
                return middle, self.which_max(middle, indexes_from_rows)
            elif (left_max > middle_max) and (left_max > right_max):
                return self.search(start, left, indexes_from_rows)
            else:
                return self.search(right, end, indexes_from_rows)

    def find_max(self, index, indexes_from_rows):
        max_val = -1
        if indexes_from_rows:
            for j in range(len(self.mat[0])):
                max_val = max(max_val, self.mat[index][j])
        else:
            for j in range(len(self.mat)):
                max_val = max(max_val, self.mat[j][index])
        return max_val

    def which_max(self, index, indexes_from_rows):
        max_val = -1
        ind = None
        if indexes_from_rows:
            for j in range(len(self.mat[0])):
                if self.mat[index][j] > max_val:
                    max_val = self.mat[index][j]
                    ind = j
            return ind
        else:
            for j in range(len(self.mat)):
                if self.mat[j][index] > max_val:
                    max_val = self.mat[j][index]
                    ind = j
            return ind
