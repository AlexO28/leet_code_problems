# There are 8 prison cells in a row and each cell is either occupied or vacant.
# Each day, whether the cell is occupied or vacant changes according to the following rules:
# If a cell has two adjacent neighbors that are both occupied or both vacant, then the cell becomes occupied.
# Otherwise, it becomes vacant.
# Note that because the prison is a row, the first and the last cells in the row can't have two adjacent neighbors.
# You are given an integer array cells where cells[i] == 1 if the ith cell is occupied and cells[i] == 0 if the ith cell is vacant, and you are given an integer n.
# Return the state of the prison after n days (i.e., n such changes described above).
from typing import List


class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        cache = []
        for j in range(n):
            try:
                ind = cache.index(cells)
                delta = j - ind
                gap = n - ind
                gap = gap % delta
                return cache[gap+ind]
            except:
                cache.append(cells.copy())
            cells_copy = cells.copy()
            cells_copy[0] = 0
            cells_copy[-1] = 0
            for i in range(1, 7):
                summa = cells[i-1] + cells[i+1]
                if (summa == 0) or (summa == 2):
                    cells_copy[i] = 1
                else:
                    cells_copy[i] = 0
            cells = cells_copy.copy()
        return cells
