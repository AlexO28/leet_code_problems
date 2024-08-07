# We stack glasses in a pyramid, where the first row has 1 glass, the second row has 2 glasses, and so on until the 100th row.  Each glass holds one cup of champagne.
# Then, some champagne is poured into the first glass at the top.  When the topmost glass is full, any excess liquid poured will fall equally to the glass immediately to the left and right of it.  When those glasses become full, any excess champagne will fall equally to the left and right of those glasses, and so on.  (A glass at the bottom row has its excess champagne fall on the floor.)
# For example, after one cup of champagne is poured, the top most glass is full.  After two cups of champagne are poured, the two glasses on the second row are half full.  After three cups of champagne are poured, those two cups become full - there are 3 full glasses total now.  After four cups of champagne are poured, the third row has the middle glass half full, and the two outside glasses are a quarter full, as pictured below.
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [[0] * 101 for j in range(min(101, query_row+2))]
        dp[0][0] = poured
        for i in range(query_row + 1):
            for j in range(i + 1):
                if dp[i][j] > 1:
                    half = (dp[i][j] - 1) / 2
                    dp[i][j] = 1
                    dp[i + 1][j] += half
                    dp[i + 1][j + 1] += half
        return dp[query_row][query_glass]
