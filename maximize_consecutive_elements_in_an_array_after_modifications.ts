/*
You are given a 0-indexed array nums consisting of positive integers.
Initially, you can increase the value of any element in the array by at most 1.
After that, you need to select one or more elements from the final array such that those elements are consecutive when sorted in increasing order. For example, the elements [3, 4, 5] are consecutive while [3, 4, 6] and [1, 1, 2, 3] are not.
Return the maximum number of elements that you can select.
*/
function maxSelectedElements(nums: number[]): number {
    nums.sort((a, b) => a - b);
    let res: number = 1;
    let prev: number = -Infinity;
    let f0: number = 1;
    let f1: number = 1;
    for (const x of nums) {
        if (x === prev) {
            f1 = f0 + 1;
        } else if (x === prev + 1) {
            ++f0;
            ++f1;
        } else if (x === prev + 2) {
            f0 = f1 + 1;
            f1 = 1;
        } else {
            f0 = 1;
            f1 = 1;
        }
        res = Math.max(res, f0, f1);
        prev = x;
    }
    return res;
};
