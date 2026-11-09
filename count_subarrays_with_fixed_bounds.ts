/*
You are given an integer array nums and two integers minK and maxK.
A fixed-bound subarray of nums is a subarray that satisfies the following conditions:
The minimum value in the subarray is equal to minK.
The maximum value in the subarray is equal to maxK.
Return the number of fixed-bound subarrays.
A subarray is a contiguous part of an array.
*/
function countSubarrays(nums: number[], minK: number, maxK: number): number {
    let res: number = 0;
    let j1: number = -1;
    let j2: number = -1;
    let k: number = -1;
    for (let i: number = 0; i < nums.length; ++i) {
        if (nums[i] < minK || nums[i] > maxK) {
            k = i;
        }
        if (nums[i] === minK) {
            j1 = i;
        }
        if (nums[i] === maxK) {
            j2 = i;
        }
        res += Math.max(0, Math.min(j1, j2) - k);
    }
    return res;
};
