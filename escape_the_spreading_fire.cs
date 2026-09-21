/*
You are given a 0-indexed 2D integer array grid of size m x n which represents a field. Each cell has one of three values:
0 represents grass,
1 represents fire,
2 represents a wall that you and fire cannot pass through.
You are situated in the top-left cell, (0, 0), and you want to travel to the safehouse at the bottom-right cell, (m - 1, n - 1). Every minute, you may move to an adjacent grass cell. After your move, every fire cell will spread to all adjacent cells that are not walls.
Return the maximum number of minutes that you can stay in your initial position before moving while still safely reaching the safehouse. If this is impossible, return -1. If you can always reach the safehouse regardless of the minutes stayed, return 109.
Note that even if the fire spreads to the safehouse immediately after you have reached it, it will be counted as safely reaching the safehouse.
A cell is adjacent to another cell if the former is directly north, east, south, or west of the latter (i.e., their sides are touching).
*/
using System.Collections.Generic;


public class Solution {
    private int[][] grid;
    private bool[][] fire;
    private bool[][] vis;
    private readonly int[] dirs = {-1, 0, 1, 0, -1};

    public int MaximumMinutes(int[][] grid) {
        this.grid = grid;
        fire = new bool[grid.Length][];
        vis = new bool[grid.Length][];
        for (int i = 0; i < grid.Length; ++i) {
            fire[i] = new bool[grid[0].Length];
        }
        for (int i = 0; i < grid.Length; ++i) {
            vis[i] = new bool[grid[0].Length];
        }
        int l = -1;
        int max = grid.Length * grid[0].Length;
        int r = max;
        while (l < r) {
            int mid = (l + r + 1) >> 1;
            if (check(mid)) {
                l = mid;
            } else {
                r = mid - 1;
            }
        }
        if (l == max) {
            return 1000000000;
        } else {
            return l;
        }
    }

    private bool check(int t) {
        for (int i = 0; i < grid.Length; ++i) {
            for (int j = 0; j < grid[0].Length; ++j) {
                fire[i][j] = false;
                vis[i][j] = false;
            }
        }
        LinkedList<int[]> q1 = new LinkedList<int[]>();
        for (int i = 0; i < grid.Length; ++i) {
            for (int j = 0; j < grid[0].Length; ++j) {
                if (grid[i][j] == 1) {
                    q1.AddLast(new int[] { i, j });
                    fire[i][j] = true;
                }
            }
        }
        for (; (t > 0) && (q1.Count > 0); --t) {
            q1 = spread(q1);
        }
        if (fire[0][0]) {
            return false;
        }
        LinkedList<int[]> q2 = new LinkedList<int[]>();
        q2.AddLast(new int[] { 0, 0 });
        vis[0][0] = true;
        for (; q2.Count > 0; q1 = spread(q1)) {
            for (int d = q2.Count; d > 0; --d) {
                int[] p = q2.First.Value;
                q2.RemoveFirst();
                if (fire[p[0]][p[1]]) {
                    continue;
                }
                for (int k = 0; k < 4; ++k) {
                    int x = p[0] + dirs[k];
                    int y = p[1] + dirs[k + 1];
                    if ((x >= 0) && (x < grid.Length) && (y >= 0) && (y < grid[0].Length) && (!fire[x][y]) && (!vis[x][y]) && (grid[x][y] == 0)) {
                        if ((x == grid.Length - 1) && (y == grid[0].Length - 1)) {
                            return true;
                        }
                        vis[x][y] = true;
                        q2.AddLast(new int[] { x, y });
                    }
                }
            }
        }
        return false;
    }

    private LinkedList<int[]> spread(LinkedList<int[]> q) {
        LinkedList<int[]> nq = new LinkedList<int[]>();
        while (q.Count > 0) {
            int[] p = q.First.Value;
            q.RemoveFirst();
            for (int k = 0; k < 4; ++k) {
                int x = p[0] + dirs[k];
                int y = p[1] + dirs[k + 1];
                if ((x >= 0) && (x < grid.Length) && (y >= 0) && (y < grid[0].Length) && (!fire[x][y]) && (grid[x][y] == 0)) {
                    fire[x][y] = true;
                    nq.AddLast(new int[] {x, y});
                }
            }
        }
        return nq;
    }
}
