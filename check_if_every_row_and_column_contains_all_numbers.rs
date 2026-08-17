/*
An n x n matrix is valid if every row and every column contains all the integers from 1 to n (inclusive).
Given an n x n integer matrix matrix, return true if the matrix is valid. Otherwise, return false.
*/
use std::collections::HashSet;


impl Solution {
    pub fn check_valid(matrix: Vec<Vec<i32>>) -> bool {
        for row in &matrix {
            let mut stats = HashSet::new();
            for &val in row {
                stats.insert(val);
            }
            if (stats.len() < matrix.len()) {
                return false;
            }
        }
        for col in 0..matrix.len() {
            let mut stats = HashSet::new();
            for row in 0..matrix.len() {
                stats.insert(matrix[row][col]);
            }
            if (stats.len() < matrix.len()) {
                return false;
            }
        }
        true
    }
}
