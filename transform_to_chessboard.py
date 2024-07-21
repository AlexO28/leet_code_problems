# You are given an n x n binary grid board. In each move, you can swap any two rows with each other, or any two columns with each other.
# Return the minimum number of moves to transform the board into a chessboard board. If the task is impossible, return -1.
# A chessboard board is a board where no 0's and no 1's are 4-directionally adjacent.
class Solution:
    def movesToChessboard(self, board: List[List[int]]) -> int:
        self.n = len(board)
        mask = (1 << self.n) - 1
        row_mask = 0
        col_mask = 0
        for i in range(self.n):
            row_mask |= board[0][i] << i
            col_mask |= board[i][0] << i
        rev_row_mask = mask ^ row_mask
        rev_col_mask = mask ^ col_mask
        same_row_count = 0
        same_col_count = 0
        for i in range(self.n):
            cur_row_mask = 0
            cur_col_mask = 0
            for j in range(self.n):
                cur_row_mask |= board[i][j] << j
                cur_col_mask |= board[j][i] << j
            if cur_row_mask not in (row_mask, rev_row_mask) or cur_col_mask not in (col_mask, rev_col_mask):
                return -1
            same_row_count += cur_row_mask == row_mask
            same_col_count += cur_col_mask == col_mask
        moves_row = self.calculate_moves(row_mask, same_row_count)
        moves_col = self.calculate_moves(col_mask, same_col_count)
        if (moves_row == -1) or (moves_col == -1):
            return -1
        else:
            return moves_row + moves_col


    def calculate_moves(self, mask, count):
        ones = mask.bit_count()  
        if self.n & 1:
            if abs(self.n - 2 * ones) != 1 or abs(self.n - 2 * count) != 1:
                return -1
            elif ones == self.n // 2:
                return self.n // 2 - (mask & 0xAAAAAAAA).bit_count()
            else:
                return (self.n + 1) // 2 - (mask & 0x55555555).bit_count()
        else:
            if ones != self.n // 2 or count != self.n // 2:
                return -1
            else:
                moves_even = self.n // 2 - (mask & 0xAAAAAAAA).bit_count()
                moves_odd = self.n // 2 - (mask & 0x55555555).bit_count()
                return min(moves_even, moves_odd)
