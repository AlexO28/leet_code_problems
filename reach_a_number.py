# You are standing at position 0 on an infinite number line. There is a destination at position target.
# You can make some number of moves numMoves so that:
# On each move, you can either go left or right.
# During the ith move (starting from i == 1 to i == numMoves), you take i steps in the chosen direction.
# Given the integer target, return the minimum number of moves required (i.e., the minimum numMoves) to reach the destination.
class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        total_sum = 0
        i = 1
        while (total_sum < target) or ((total_sum - target) % 2 == 1):
            total_sum += i
            i += 1
        return i-1
