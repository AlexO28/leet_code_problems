/*
There is an m x n grid, where (0, 0) is the top-left cell and (m - 1, n - 1) is the bottom-right cell. You are given an integer array startPos where startPos = [startrow, startcol] indicates that initially, a robot is at the cell (startrow, startcol). You are also given an integer array homePos where homePos = [homerow, homecol] indicates that its home is at the cell (homerow, homecol).
The robot needs to go to its home. It can move one cell in four directions: left, right, up, or down, and it can not move outside the boundary. Every move incurs some cost. You are further given two 0-indexed integer arrays: rowCosts of length m and colCosts of length n.
If the robot moves up or down into a cell whose row is r, then this move costs rowCosts[r].
If the robot moves left or right into a cell whose column is c, then this move costs colCosts[c].
Return the minimum total cost for this robot to return home.
*/
public class Solution {
    public int MinCost(int[] startPos, int[] homePos, int[] rowCosts, int[] colCosts) {
        int x0 = startPos[0];
        int y0 = startPos[1];
        int x1 = homePos[0];
        int y1 = homePos[1];
        int dx = (x0 < x1) ? calc(rowCosts, x0 + 1, x1) : calc(rowCosts, x1, x0 - 1);
        int dy = (y0 < y1) ? calc(colCosts, y0 + 1, y1) : calc(colCosts, y1, y0 - 1);
        return dx + dy;
    }

    private int calc(int[] nums, int i , int j) {
        int res = 0;
        for (int k = i; k <= j; ++k) {
            res += nums[k];
        }
        return res;
    }
}
