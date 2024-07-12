# On an 2 x 3 board, there are five tiles labeled from 1 to 5, and an empty square represented by 0. A move consists of choosing 0 and a 4-directionally adjacent number and swapping it.
# The state of the board is solved if and only if the board is [[1,2,3],[4,5,0]].
# Given the puzzle board board, return the least number of moves required so that the state of the board is solved. If it is impossible for the state of the board to be solved, return -1.
class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        self.vis = {}
        self.dir = [1, 0, -1, 0, 1]
        if self.__check(board):
            return 0
        queue = []
        st = self.__board_to_string(board)
        queue.append(st)
        self.vis[st] = 1
        step = 0
        while len(queue) > 0:
            size = len(queue)
            for cur_size in range(size, 0, -1):
                current = queue[0]
                del queue[0]
                index = 0
                stx = 0
                sty = 0
                for i in range(2):
                    for j in range(3):
                        board[i][j] = int(current[index])
                        index += 1
                        if board[i][j] == 0:
                            stx = i
                            sty = j
                for i in range(4):
                    nx = stx + self.dir[i]
                    ny = sty + self.dir[i+1]
                    if not ((nx < 0) or (nx >= 2) or (ny < 0) or (ny >= 3)):
                        temp = board[nx][ny]
                        board[nx][ny] = 0
                        board[stx][sty] = temp
                        if self.__check(board):
                            return step + 1
                        tt = self.__board_to_string(board)
                        if tt in self.vis:
                            board[nx][ny] = temp
                            board[stx][sty] = 0
                        else:
                            self.vis[tt] = 1
                            queue.append(tt)
                            board[nx][ny] = temp
                            board[stx][sty] = 0
            step += 1
        return -1

    def __board_to_string(self, board):
        st = ""
        for i in range(2):
            for j in range(3):
                st += str(board[i][j])
        return st

    def __check(self, board):
        st = 1
        for i in range(2):
            for j in range(3):
                if (i == 1) and (j == 2):
                    if (board[i][j] != 0):
                        return False
                else:
                    if board[i][j] != st:
                        return False
                    else:
                        st += 1
        return True
