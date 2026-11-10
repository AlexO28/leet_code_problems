/*
You are given two positive integer arrays nums and target, of the same length.
In one operation, you can choose any two distinct indices i and j where 0 <= i, j < nums.length and:
set nums[i] = nums[i] + 2 and
set nums[j] = nums[j] - 2.
Two arrays are considered to be similar if the frequency of each element is the same.
Return the minimum number of operations required to make nums similar to target. The test cases are generated such that nums can always be similar to target.
*/
function makeSimilar(nums: number[], target: number[]): number {
    nums.sort((a, b) => a - b);
    target.sort((a, b) => a - b);
    const a1: number[] = [];
    const a2: number[] = [];
    const b1: number[] = [];
    const b2: number[] = [];
    for (const v of nums) {
        if (v % 2 === 0) {
            a1.push(v);
        } else {
            a2.push(v);
        }
    }
    for (const v of target) {
        if (v % 2 === 0) {
            b1.push(v);
        } else {
            b2.push(v);
        }
    }
    let res: number = 0;
    for (let i = 0; i < a1.length; ++i) {
        res += Math.abs(a1[i] - b1[i]);
    }
    for (let i = 0; i < a2.length; ++i) {
        res += Math.abs(a2[i] - b2[i]);
    }
    return res / 4;
};
