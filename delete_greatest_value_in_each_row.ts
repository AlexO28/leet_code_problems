/*
You are given an m x n matrix grid consisting of positive integers.
Perform the following operation until grid becomes empty:
Delete the element with the greatest value from each row. If multiple such elements exist, delete any of them.
Add the maximum of deleted elements to the answer.
Note that the number of columns decreases by one after each operation.
Return the answer after performing the operations described above.
*/
function deleteGreatestValue(grid: number[][]): number {
    grid = grid.map((row) => row.toSorted((a, b) => a - b));
    let res: number = 0;
    for (let i: number = 0; i < grid[0].length; ++i) {
        let maxVal : number = -1;
        for (let j: number = 0; j < grid.length; ++j) {
            maxVal = Math.max(maxVal, grid[j][i]);
        }
        res += maxVal;
    }
    return res;
};
