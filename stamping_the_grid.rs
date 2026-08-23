/*
You are given an m x n binary matrix grid where each cell is either 0 (empty) or 1 (occupied).
You are then given stamps of size stampHeight x stampWidth. We want to fit the stamps such that they follow the given restrictions and requirements:
Cover all the empty cells.
Do not cover any of the occupied cells.
We can put as many stamps as we want.
Stamps can overlap with each other.
Stamps are not allowed to be rotated.
Stamps must stay completely inside the grid.
Return true if it is possible to fit the stamps while following the given restrictions and requirements. Otherwise, return false.
*/
impl Solution {
    pub fn possible_to_stamp(grid: Vec<Vec<i32>>, stamp_height: i32, stamp_width: i32) -> bool {
        if stamp_height as usize > grid.len() || stamp_width as usize > grid[0].len() {
            for i in 0..grid.len() {
                for j in 0..grid[0].len() {
                    if grid[i][j] == 0 {
                        return false;
                    }
                }
            }
            return true;
        }
        let mut mat = vec![vec![0; grid[0].len() + 1]; grid.len() + 1];
        for i in 0..grid.len() {
            for j in 0..grid[0].len() {
                mat[i + 1][j + 1] = mat[i][j + 1] + mat[i + 1][j] - mat[i][j] + grid[i][j];
            }
        }
        let mut d = vec![vec![0; grid[0].len() + 2]; grid.len() + 2];
        for i in 1..(grid.len() - stamp_height as usize + 2) {
            for j in 1..(grid[0].len() - stamp_width as usize + 2) {
                let x = i + stamp_height as usize - 1;
                let y = j + stamp_width as usize - 1;
                if (mat[x][y] - mat[x][j - 1] - mat[i - 1][y] + mat[i - 1][j - 1] == 0) {
                    d[i][j] += 1;
                    d[i][y + 1] -= 1;
                    d[x + 1][j] -= 1;
                    d[x + 1][y + 1] += 1;
                }
            }
        }
        for i in 0..grid.len() {
            for j in 0..grid[0].len() {
                d[i + 1][j + 1] += d[i][j + 1] + d[i + 1][j] - d[i][j];
                if (grid[i][j] == 0) && (d[i + 1][j + 1] == 0) {
                    return false;
                } 
            }
        }
        return true;
    }
}
