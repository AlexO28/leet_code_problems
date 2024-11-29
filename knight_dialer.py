# The chess knight has a unique movement, it may move two squares vertically and one square horizontally, or two squares horizontally and one square vertically (with both forming the shape of an L). The possible movements of chess knight are shown in this diagram:
# We have a chess knight and a phone pad as shown below, the knight can only stand on a numeric cell (i.e. blue cell).
# Given an integer n, return how many distinct phone numbers of length n we can dial.
# You are allowed to place the knight on any numeric cell initially and then you should perform n - 1 jumps to dial a number of length n. All jumps should be valid knight jumps.
# As the answer may be very large, return the answer modulo 109 + 7.
class Solution:
    def knightDialer(self, n: int) -> int:
        if n == 1:
            return 10
        counts = [1] * 10
        for i in range(n - 1):
            temp_counts = [0] * 10
            temp_counts[0] = counts[4] + counts[6]
            temp_counts[1] = counts[6] + counts[8]
            temp_counts[2] = counts[7] + counts[9]
            temp_counts[3] = counts[4] + counts[8]
            temp_counts[4] = counts[0] + counts[3] + counts[9]
            temp_counts[6] = counts[0] + counts[1] + counts[7]
            temp_counts[7] = counts[2] + counts[6]
            temp_counts[8] = counts[1] + counts[3]
            temp_counts[9] = counts[2] + counts[4]
            counts = temp_counts
        return sum(counts) % (10 ** 9 + 7)
