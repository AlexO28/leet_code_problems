# You are given an n x n integer matrix board where the cells are labeled from 1 to n2 in a Boustrophedon style starting from the bottom left of the board (i.e. board[n - 1][0]) and alternating direction each row.
# You start on square 1 of the board. In each move, starting from square curr, do the following:
# Choose a destination square next with a label in the range [curr + 1, min(curr + 6, n2)].
# This choice simulates the result of a standard 6-sided die roll: i.e., there are always at most 6 destinations, regardless of the size of the board.
# If next has a snake or ladder, you must move to the destination of that snake or ladder. Otherwise, you move to next.
# The game ends when you reach the square n2.
# A board square on row r and column c has a snake or ladder if board[r][c] != -1. The destination of that snake or ladder is board[r][c]. Squares 1 and n2 are not the starting points of any snake or ladder.
# Note that you only take a snake or ladder at most once per dice roll. If the destination to a snake or ladder is the start of another snake or ladder, you do not follow the subsequent snake or ladder.
# For example, suppose the board is [[-1,4],[-1,3]], and on the first move, your destination square is 2. You follow the ladder to square 3, but do not follow the subsequent ladder to 4.
# Return the least number of dice rolls required to reach the square n2. If it is not possible to reach the square, return -1.
from collections import deque


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        queue = deque([1])
        visited = {1}
        steps = 0
        self.board_size = len(board)
        max_size = self.board_size ** 2
        while queue:
            for i in range(len(queue)):
                current_square = queue.popleft()
                if current_square == max_size:
                    return steps
                else:
                    for next_square in range(current_square+1, min(current_square+7, 1 + max_size)):
                        i, j = self.get_coordinates(next_square)
                        if board[i][j] > 0:
                            next_square = board[i][j]
                        if next_square not in visited:
                            queue.append(next_square)
                            visited.add(next_square)
            steps += 1
        return -1


    def get_coordinates(self, square):
        row, col = divmod(square-1, self.board_size)
        if row % 2 == 1:
            return self.board_size-1-row, self.board_size-1-col
        else:
            return self.board_size-1-row, col
