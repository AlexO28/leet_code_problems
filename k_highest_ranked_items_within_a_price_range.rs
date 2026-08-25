/*
You are given a 0-indexed 2D integer array grid of size m x n that represents a map of the items in a shop. The integers in the grid represent the following:
0 represents a wall that you cannot pass through.
1 represents an empty cell that you can freely move to and from.
All other positive integers represent the price of an item in that cell. You may also freely move to and from these item cells.
It takes 1 step to travel between adjacent grid cells.
You are also given integer arrays pricing and start where pricing = [low, high] and start = [row, col] indicates that you start at the position (row, col) and are interested only in items with a price in the range of [low, high] (inclusive). You are further given an integer k.
You are interested in the positions of the k highest-ranked items whose prices are within the given price range. The rank is determined by the first of these criteria that is different:
Distance, defined as the length of the shortest path from the start (shorter distance has a higher rank).
Price (lower price has a higher rank, but it must be in the price range).
The row number (smaller row number has a higher rank).
The column number (smaller column number has a higher rank).
Return the k highest-ranked items within the price range sorted by their rank (highest to lowest). If there are fewer than k reachable items within the price range, return all of them.
*/
use std::collections::VecDeque;


impl Solution {
    pub fn highest_ranked_k_items(grid: Vec<Vec<i32>>, pricing: Vec<i32>, start: Vec<i32>, k: i32) -> Vec<Vec<i32>> {
        let mut grid = grid;
        let mut q: VecDeque<Vec<i32>> = VecDeque::new();
        q.push_back(vec![start[0], start[1]]);
        let mut pq: Vec<Vec<i32>> = Vec::new();
        if (pricing[0] <= grid[start[0] as usize][start[1] as usize]) && (grid[start[0] as usize][start[1] as usize] <= pricing[1]) {
            pq.push(vec![0, grid[start[0] as usize][start[1] as usize], start[0], start[1]]);
        }
        grid[start[0] as usize][start[1] as usize] = 0;
        let dirs: Vec<i32> = vec![-1, 0, 1, 0, -1];
        let mut step = 1;
        loop {
            if q.is_empty() {
                break;
            } else {
                for size in (0..q.len()).rev() {
                    let curr = q.pop_front().unwrap();
                    for j in 0..4 {
                        let nx = curr[0] + dirs[j];
                        let ny = curr[1] + dirs[j + 1];
                        if (0 <= nx) && (nx < grid.len() as i32) && (0 <= ny) && (ny < grid[0].len() as i32 && (grid[nx as usize][ny as usize] > 0)) {
                            if (pricing[0] <= grid[nx as usize][ny as usize]) && (grid[nx as usize][ny as usize] <= pricing[1]) {
                                pq.push(vec![step, grid[nx as usize][ny as usize], nx, ny]);
                            }
                            grid[nx as usize][ny as usize] = 0;
                            q.push_back(vec![nx, ny]);
                        }
                    }
                }
                step += 1;
            }
        }
        pq.sort();
        let mut ans: Vec<Vec<i32>> = Vec::new();
        for i in 0..k.min(pq.len() as i32) {
            ans.push(vec![pq[i as usize][2], pq[i as usize][3]]);
        }
        ans
    }
}
