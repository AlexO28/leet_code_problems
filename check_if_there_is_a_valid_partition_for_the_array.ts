/*
You are given a 0-indexed integer array nums. You have to partition the array into one or more contiguous subarrays.
We call a partition of the array valid if each of the obtained subarrays satisfies one of the following conditions:
The subarray consists of exactly 2, equal elements. For example, the subarray [2,2] is good.
The subarray consists of exactly 3, equal elements. For example, the subarray [4,4,4] is good.
The subarray consists of exactly 3 consecutive increasing elements, that is, the difference between adjacent elements is 1. For example, the subarray [3,4,5] is good, but the subarray [1,3,5] is not.
Return true if the array has at least one valid partition. Otherwise, return false.
*/
function validPartition(nums: number[]): boolean {
    const f: number[] = Array(nums.length).fill(-1);
    return search(0, nums, f);
};

function search(i: number, nums: number[], f: number[]): boolean {
    if (i >= nums.length) {
        return true;
    }
    if (f[i] !== -1) {
        return f[i] === 1;
    }
    const a = i + 1 < nums.length && nums[i] === nums[i + 1];
    const b = i + 2 < nums.length && nums[i] === nums[i + 1] && nums[i + 1] === nums[i + 2];
    const c = i + 2 < nums.length && nums[i + 1] - nums[i] === 1 && nums[i + 2] - nums[i + 1] === 1;
    f[i] = (a && search(i + 2, nums, f)) || ((b || c) && search(i + 3, nums, f)) ? 1 : 0;
    return f[i] === 1;
};
