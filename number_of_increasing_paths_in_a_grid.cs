/*
You are given an m x n integer matrix grid, where you can move from a cell to any adjacent cell in all 4 directions.
Return the number of strictly increasing paths in the grid such that you can start from any cell and end at any cell. Since the answer may be very large, return it modulo 109 + 7.
Two paths are considered different if they do not have exactly the same sequence of visited cells.
*/
public class Solution {
    private int[,] f;
    private int[][] grid;
    private const int mod = 1000000007;

    public int CountPaths(int[][] grid) {
        this.grid = grid;
        f = new int[grid.Length, grid[0].Length];
        int res = 0;
        for (int i = 0; i < grid.Length; ++i) {
            for (int j = 0; j < grid[0].Length; ++j) {
                res = (res + search(i, j)) % mod;
            }
        }
        return res;
    }

    private int search(int i, int j) {
        if (f[i, j] != 0) {
            return f[i, j];
        }
        int res = 1;
        int[] dirs = {-1, 0, 1, 0, -1};
        for (int k = 0; k < 4; ++k) {
            int x = i + dirs[k];
            int y = j + dirs[k + 1];
            if (x >= 0 && x < grid.Length && y >= 0 && y < grid[0].Length && grid[i][j] < grid[x][y]) {
                res = (res + search(x, y)) % mod;
            }
        }
        return f[i, j] = res;
    }
}
