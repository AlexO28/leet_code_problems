# Given a rectangle of size n x m, return the minimum number of integer-sided squares that tile the rectangle.
class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        self.min_tiles = m * n
        self.filled = [0] * n
        self.n = n
        self.m = m
        self.search(0, 0, 0)
        return self.min_tiles

    def search(self, row, col, tiles_used):
        if col == self.m:
            row += 1
            col = 0
        if row == self.n:
            self.min_tiles = tiles_used
        else:
            if self.filled[row] >> col & 1:
                self.search(row, col + 1, tiles_used)
            elif tiles_used + 1 < self.min_tiles:
                max_row = 0
                max_col = 0
                for k in range(row, self.n):
                    if self.filled[k] >> col & 1:
                        break
                    max_row += 1
                for k in range(col, self.m):
                    if self.filled[row] >> k & 1:
                        break
                    max_col += 1
                max_tile_size = min(max_row, max_col)
                for x in range(row, row + max_tile_size):
                    for y in range(col, col + max_tile_size):
                        self.filled[x] |= 1 << y
                for width in range(max_tile_size, 0, -1):
                    self.search(row, col + width, tiles_used + 1)
                    for k in range(width):
                        self.filled[row + width - 1] ^= 1 << (col + k)
                        if k < width - 1:
                            self.filled[row + k] ^= 1 << (col + width - 1)
