# You have a grid of size n x 3 and you want to paint each cell of the grid with exactly one of the three colors: Red, Yellow, or Green while making sure that no two adjacent cells have the same color (i.e., no two cells that share vertical or horizontal sides have the same color).
# Given n the number of rows of the grid, return the number of ways you can paint this grid. As the answer may grow large, the answer must be computed modulo 109 + 7.
class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10**9 + 7
        aba_pattern_count = 6
        abc_pattern_count = 6
        for j in range(n - 1):
            next_aba_count = (3 * aba_pattern_count + 2 * abc_pattern_count) % MOD
            next_abc_count = (2 * aba_pattern_count + 2 * abc_pattern_count) % MOD
            aba_pattern_count = next_aba_count
            abc_pattern_count = next_abc_count
        return (aba_pattern_count + abc_pattern_count) % MOD
