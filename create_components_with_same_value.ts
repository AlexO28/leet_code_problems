/*
There is an undirected tree with n nodes labeled from 0 to n - 1.
You are given a 0-indexed integer array nums of length n where nums[i] represents the value of the ith node. You are also given a 2D integer array edges of length n - 1 where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree.
You are allowed to delete some edges, splitting the tree into multiple connected components. Let the value of a component be the sum of all nums[i] for which node i is in the component.
Return the maximum number of edges you can delete, such that every connected component in the tree has the same value.
*/
let g: number[][];
let numsGlobal: number[];
let t: number;


function componentValue(nums: number[], edges: number[][]): number {
    g = Array.from({ length: nums.length }, () => []);
    numsGlobal = nums;
    for (const edge of edges) {
        g[edge[0]].push(edge[1]);
        g[edge[1]].push(edge[0]);
    }
    let s: number = 0;
    let m: number = 0;
    for (const num of nums) {
        s += num;
        m = Math.max(m, num);
    }
    for (let k: number = Math.min(nums.length, Math.floor(s / m)); k > 1; --k) {
        if (s % k == 0) {
            t = s / k;
            if (search(0, -1) == 0) {
                return k - 1;
            }
        }
    }
    return 0;
};


function search(i: number, fa: number): number {
    let x: number = numsGlobal[i];
    for (const j of g[i]) {
        if (j != fa) {
            let y: number = search(j, i);
            if (y == -1) {
                return -1;
            } else {
                x += y;
            }
        }
    }
    if (x > t) {
        return -1;
    } else {
        return x < t ? x : 0;
    }
};
