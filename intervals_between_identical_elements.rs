/*
You are given a 0-indexed array of n integers arr.
The interval between two elements in arr is defined as the absolute difference between their indices. More formally, the interval between arr[i] and arr[j] is |i - j|.
Return an array intervals of length n where intervals[i] is the sum of intervals between arr[i] and each element in arr with the same value as arr[i].
Note: |x| is the absolute value of x.
*/
use std::collections::HashMap;


impl Solution {
    pub fn get_distances(arr: Vec<i32>) -> Vec<i64> {
        let mut freqs: HashMap<i32, Vec<i32>> = HashMap::new();
        for i in 0..arr.len() {
            freqs.entry(arr[i]).or_default().push(i as i32);
        }
        let mut res = vec![0; arr.len()];
        for (key, list) in &freqs {
            let mut val: i64 = list.iter().map(|&x| x as i64).sum::<i64>() - (list[0] as i64) * (list.len() as i64);
            for (index, value) in list.iter().enumerate() {
                let mut delta: i64 = 0;
                if index >= 1 {
                    delta = list[index] as i64 - list[index - 1] as i64;
                }
                val += (index as i64) * delta - (list.len() as i64 - index as i64) * delta;
                res[*value as usize] = val;
            }
        }
        return res;
    }
}
