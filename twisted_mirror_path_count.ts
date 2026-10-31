/*
Given an m x n binary grid grid where:
grid[i][j] == 0 represents an empty cell, and
grid[i][j] == 1 represents a mirror.
A robot starts at the top-left corner of the grid (0, 0) and wants to reach the bottom-right corner (m - 1, n - 1). It can move only right or down. If the robot attempts to move into a mirror cell, it is reflected before entering that cell:
If it tries to move right into a mirror, it is turned down and moved into the cell directly below the mirror.
If it tries to move down into a mirror, it is turned right and moved into the cell directly to the right of the mirror.
If this reflection would cause the robot to move outside the grid boundaries, the path is considered invalid and should not be counted.
Return the number of unique valid paths from (0, 0) to (m - 1, n - 1).
Since the answer may be very large, return it modulo 109 + 7.
Note: If a reflection moves the robot into a mirror cell, the robot is immediately reflected again based on the direction it used to enter that mirror: if it entered while moving right, it will be turned down; if it entered while moving down, it will be turned right. This process will continue until either the last cell is reached, the robot moves out of bounds or the robot moves to a non-mirror cell.
*/
function uniquePaths(grid: number[][]): number {
    const MOD: number = 1000000007;
    const dp: number[][] = Array.from({ length:  Math.min(grid.length, grid[0].length) + 1 }, () => [0, 0]);
    dp[1] = [1, 1];
    for (let right: number = 0; right < Math.max(grid.length, grid[0].length); ++right) {
        for (let center: number = 0; center < dp.length - 1; ++center) {
            let temp: number;
            if (grid.length > grid[0].length) {
                temp = grid[right][center];
            } else {
                temp = grid[center][right];
            }
            let c: number = center + 1;
            if (temp > 0) {
                dp[c] = [dp[c][1], dp[center][0]]
            } else {
                const val: number = (dp[c][1] + dp[center][0]) % MOD;
                dp[c] = [val, val];
            }
        }
    }
    return dp[dp.length - 1][0];
};
