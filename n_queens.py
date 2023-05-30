# return all solutions of n queens problems for n between 1 and 9


def initialize_the_board(n):
    board = ['.'*n]*n
    return board


def change_position_in_str(line, pos, symb):
    temp_list = list(line)
    temp_list[pos] = symb
    return ''.join(temp_list)


def solve_queens_for_row(board, row_num):
    n = len(board)
    all_solutions = []
    for j in range(n):
        if check_disposition(board, row_num, j) == True:
            board[row_num] = change_position_in_str(board[row_num], j, 'Q')
            if row_num < n - 1:
                solutions = solve_queens_for_row(board, row_num + 1)
                if len(solutions[0]) > 0:
                    for solution in solutions:
                        new_solution = []
                        for k in range(n):
                            if k == j:
                                new_solution.append('Q' + str(solution[k]))
                            else:
                                new_solution.append('.' +
                                    str(solution[k]))                        
                        all_solutions.append(new_solution)
            else:                        
                temp_list = ['.']*n
                temp_list[j] = 'Q'
                all_solutions.append(temp_list)
        board[row_num] = change_position_in_str(board[row_num], j, '.')
    if len(all_solutions) == 0:
        return [[]]
    return all_solutions


def check_disposition(board, i, j):
    n = len(board)
    if i > 0:
        for k in range(i):
            if 'Q' in list(board[k])[j]:
                return False
    if i > 0:
        check_vec = []
        for k in range(1, i+1):
            if j-k >= 0:
                check_vec.append(list(board[i-k])[j-k])
            if j+k < n:
                check_vec.append(list(board[i-k])[j+k])
        if 'Q' in check_vec:
            return False
    return True

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n == 1:
            return [['Q']]
        board = initialize_the_board(n)
        solutions = solve_queens_for_row(board, 0)
        if solutions == [[]]:
            return []
        return solutions
