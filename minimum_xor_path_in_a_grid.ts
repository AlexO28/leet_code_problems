/*
You are given a 2D integer array grid of size m * n.
You start at the top-left cell (0, 0) and want to reach the bottom-right cell (m - 1, n - 1).
At each step, you may move either right or down.
The cost of a path is defined as the bitwise XOR of all the values in the cells along that path, including the start and end cells.
Return the minimum possible XOR value among all valid paths from (0, 0) to (m - 1, n - 1).
*/
function minCost(grid: number[][]): number {
    let mx: number = 0;
    for (const row of grid) {
        for (const x of row) {
            mx = Math.max(mx, x);
        }
    }
    mx = 1 << (32 - Math.clz32(mx));
    const f: boolean[][][] = Array.from({ length: grid.length }, () =>
        Array.from({ length: grid[0].length }, () => new Array<boolean>(mx).fill(false)),
    );
    f[0][0][grid[0][0]] = true;
    for (let i: number = 0; i < grid.length; ++i) {
        for (let j: number = 0; j < grid[0].length; ++j) {
            const x: number = grid[i][j];
            if (i > 0 || j > 0) {
                for (let k: number = 0; k < mx; ++k) {
                    if (i > 0 && f[i - 1][j][k ^ x]) {
                        f[i][j][k] = true;
                    }
                    if (j > 0 && f[i][j - 1][k ^ x]) {
                        f[i][j][k] = true;
                    }
                }
            }
        }
    }
    for (let k: number = 0; ; ++k) {
        if (f[grid.length - 1][grid[0].length - 1][k]) {
            return k;
        }
    }
};
