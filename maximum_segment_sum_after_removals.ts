/*
You are given two 0-indexed integer arrays nums and removeQueries, both of length n. For the ith query, the element in nums at the index removeQueries[i] is removed, splitting nums into different segments.
A segment is a contiguous sequence of positive integers in nums. A segment sum is the sum of every element in a segment.
Return an integer array answer, of length n, where answer[i] is the maximum segment sum after applying the ith removal.
Note: The same index will not be removed more than once.
*/
function maximumSegmentSum(nums: number[], removeQueries: number[]): number[] {
    let p: number[] = [...Array(nums.length).keys()];
    let s: number[] = Array(nums.length).fill(0);
    let res: number[] = Array(nums.length).fill(0);
    let maxVal: number = 0;
    for (let j = nums.length - 1; j > 0; --j) {
        let i: number = removeQueries[j];
        s[i] = nums[i];
        if (i && s[find(i - 1, p)]) {
            merge(i, i - 1, p, s);
        };
        if ((i < nums.length - 1) && s[find(i + 1, p)]) {
            merge(i, i + 1, p, s);
        };
        maxVal = Math.max(maxVal, s[find(i, p)]);
        res[j - 1] = maxVal;
    };
    return res;
};

function merge(a: number, b: number, p: number[], s: number[]): void {
    let pa: number = find(a, p);
    let pb: number = find(b, p);
    p[pa] = pb;
    s[pb] += s[pa];
};

function find(x: number, p: number[]): number {
    if (p[x] != x) {
        p[x] = find(p[x], p);
    };
    return p[x];
};
