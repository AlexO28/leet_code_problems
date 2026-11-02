/*
You are given two 0-indexed arrays, nums1 and nums2, consisting of non-negative integers. Let there be another array, nums3, which contains the bitwise XOR of all pairings of integers between nums1 and nums2 (every integer in nums1 is paired with every integer in nums2 exactly once).
Return the bitwise XOR of all integers in nums3.
*/
function xorAllNums(nums1: number[], nums2: number[]): number {
    let res: number = 0;
    if (nums2.length % 2 > 0) {
        res ^= nums1.reduce((a, b) => a ^ b, 0);
    }
    if (nums1.length % 2 > 0) {
        res ^= nums2.reduce((a, b) => a ^ b, 0);
    }
    return res;
};
