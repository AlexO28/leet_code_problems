/*
You are given an integer array nums and two integers l and r. Your task is to find the minimum sum of a subarray whose size is between l and r (inclusive) and whose sum is greater than 0.
Return the minimum sum of such a subarray. If no such subarray exists, return -1.
A subarray is a contiguous non-empty sequence of elements within an array.
*/
function minimumSumSubarray(nums: number[], l: number, r: number): number {
    let bestsum: number = Number.POSITIVE_INFINITY;
    for (let i: number = 0; i < nums.length; ++i) {
        let cursum: number = 0;
        let count: number = 0;
        for (let j: number = i; j < nums.length; ++j) {
            ++count;
            if (count > r) {
                break;
            }
            cursum += nums[j];
            if ((count >= l) && (cursum > 0)) {
                bestsum = Math.min(bestsum, cursum);
            }
        }
    }
    return bestsum < Number.POSITIVE_INFINITY ? bestsum : -1;
};
