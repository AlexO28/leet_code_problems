/*You are given a 0-indexed m x n integer matrix grid and an integer k. You are currently at position (0, 0) and you want to reach position (m - 1, n - 1) moving only down or right.
Return the number of paths where the sum of the elements on the path is divisible by k. Since the answer may be very large, return it modulo 109 + 7.*/
function numberOfPaths(grid: number[][], k: number): number {
    const MOD: number = 1000000007;
    const f: number[][][] = Array.from({ length: grid.length }, () =>
        Array.from({ length: grid[0].length }, () => Array(k).fill(0)),
    );
    f[0][0][grid[0][0] % k] = 1;
    for (let x: number = 0; x < grid.length; ++x) {
        for (let y: number = 0; y < grid[0].length; ++y) {
            for (let z: number = 0; z < k; ++z) {
                const zz: number = (z - (grid[x][y] % k) + k) % k;
                if (x > 0) {
                    f[x][y][z] = (f[x][y][z] + f[x - 1][y][zz]) % MOD;
                }
                if (y > 0) {
                    f[x][y][z] = (f[x][y][z] + f[x][y - 1][zz]) % MOD;
                }
            }
        }
    }
    return f[grid.length - 1][grid[0].length - 1][0];
};
