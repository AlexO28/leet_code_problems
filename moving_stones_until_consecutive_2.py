# There are some stones in different positions on the X-axis. You are given an integer array stones, the positions of the stones.
# Call a stone an endpoint stone if it has the smallest or largest position. In one move, you pick up an endpoint stone and move it to an unoccupied position so that it is no longer an endpoint stone.
# In particular, if the stones are at say, stones = [1,2,5], you cannot move the endpoint stone at position 5, since moving it to any position (such as 0, or 3) will still keep that stone as an endpoint stone.
# The game ends when you cannot make any more moves (i.e., the stones are in three consecutive positions).
# Return an integer array answer of length 2 where:
# answer[0] is the minimum number of moves you can play, and
# answer[1] is the maximum number of moves you can play.
from typing import List


class Solution:
    def numMovesStonesII(self, stones: List[int]) -> List[int]:
        stones.sort()
        min_moves = len(stones)
        max_moves = max(stones[-1] - stones[1] - len(stones) + 2, 
                        stones[-2] - stones[0] - len(stones) + 2)
        i = 0
        for j in range(len(stones)):
            while stones[j] - stones[i] + 1 > len(stones):
                i += 1
            if (j - i + 1 == len(stones) - 1) and (stones[j] - stones[i] == len(stones) - 2):
                min_moves = min(min_moves, 2)
            else:
                min_moves = min(min_moves, len(stones) - (j - i + 1))
        return [min_moves, max_moves]
