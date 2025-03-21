# There are three stones in different positions on the X-axis. You are given three integers a, b, and c, the positions of the stones.
# In one move, you pick up a stone at an endpoint (i.e., either the lowest or highest position stone), and move it to an unoccupied position between those endpoints. Formally, let's say the stones are currently at positions x, y, and z with x < y < z. You pick up the stone at either position x or position z, and move that stone to an integer position k, with x < k < z and k != y.
# The game ends when you cannot make any more moves (i.e., the stones are in three consecutive positions).
# Return an integer array answer of length 2 where:
# answer[0] is the minimum number of moves you can play, and
# answer[1] is the maximum number of moves you can play.
class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        vals = [a, b, c]
        vals.sort()
        if vals[2] - vals[0] == 2:
            return [0, 0]
        elif vals[1] - vals[0] == 1:
            return [1, vals[2] - vals[1] - 1]
        elif vals[2] - vals[1] == 1:
            return [1, vals[1] - vals[0] - 1]
        else:
            if (vals[2] - vals[1] == 2) or (vals[1] - vals[0] == 2):
                return [1, vals[2] - vals[0] - 2]
            else:
                return [2, vals[2] - vals[0] - 2]
