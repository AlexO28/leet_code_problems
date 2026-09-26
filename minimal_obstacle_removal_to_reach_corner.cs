/*
You are given a 0-indexed 2D integer array grid of size m x n. Each cell has one of two values:
0 represents an empty cell,
1 represents an obstacle that may be removed.
You can move up, down, left, or right from and to an empty cell.
Return the minimum number of obstacles to remove so you can move from the upper left corner (0, 0) to the lower right corner (m - 1, n - 1).
*/
using System.Collections.Generic;


public class Solution {
    public int MinimumObstacles(int[][] grid) {
        LinkedList<int[]> q = new LinkedList<int[]>();
        q.AddLast(new int[] { 0, 0, 0 });
        int[] dirs = {-1, 0, 1, 0, -1};
        bool[][] vis = new bool[grid.Length][];
        for (int i = 0; i < grid.Length; ++i) {
            vis[i] = new bool[grid[0].Length];
        }
        while (true) {
            int[] p = q.First.Value;
            q.RemoveFirst();
            if ((p[0] == grid.Length - 1) && (p[1] == grid[0].Length - 1)) {
                return p[2];
            }
            if (!vis[p[0]][p[1]]) {
                vis[p[0]][p[1]] = true;
                for (int h = 0; h < 4; ++h) {
                    int x = p[0] + dirs[h];
                    int y = p[1] + dirs[h + 1];
                    if ((x >= 0) && (x < grid.Length) && (y >= 0) && (y < grid[0].Length)) {
                        if (grid[x][y] == 0) {
                            q.AddFirst(new int[] {x, y, p[2]});
                        } else {
                            q.AddLast(new int[] {x, y, p[2] + 1});
                        }
                    }
                }
            }
        }
    }
}
