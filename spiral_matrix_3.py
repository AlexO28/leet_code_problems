# You start at the cell (rStart, cStart) of an rows x cols grid facing east. The northwest corner is at the first row and column in the grid, and the southeast corner is at the last row and column.
# You will walk in a clockwise spiral shape to visit every position in this grid. Whenever you move outside the grid's boundary, we continue our walk outside the grid (but may return to the grid boundary later.). Eventually, we reach all rows * cols spaces of the grid.
# Return an array of coordinates representing the positions of the grid in the order you visited them.
class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        res = []
        order = 0
        while len(res) < rows*cols:
            if order == 0:
                res.append([rStart, cStart])
                order += 1
            else:
                init_x = rStart
                init_y = cStart + order
                if (init_x < rows) and (init_y < cols):
                    res.append([init_x, init_y])
                for j in range(order):
                    init_x += 1
                    if (init_x < rows) and (init_y >= 0) and (init_x >= 0) and (init_y < cols):
                        res.append([init_x, init_y])
                for j in range(2*order):
                    init_y -= 1
                    if (init_x < rows) and (init_y >= 0) and (init_x >= 0) and (init_y < cols):
                        res.append([init_x, init_y])
                for j in range(2*order):
                    init_x -= 1
                    if (init_x < rows) and (init_y >= 0) and (init_x >= 0) and (init_y < cols):
                        res.append([init_x, init_y])
                for j in range(2*order+1):
                    init_y += 1
                    if (init_x < rows) and (init_y >= 0) and (init_x >= 0) and (init_y < cols):
                        res.append([init_x, init_y])
                if order > 1:
                    for j in range(order-1):
                        init_x += 1
                        if (init_x < rows) and (init_y >= 0) and (init_x >= 0) and (init_y < cols):
                            res.append([init_x, init_y])
                order += 1
        return res
