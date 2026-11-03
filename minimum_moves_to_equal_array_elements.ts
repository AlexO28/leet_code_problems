/*
You are given an integer array nums.
In one move, you may increase the value of any single element nums[i] by 1.
Return the minimum total number of moves required so that all elements in nums become equal.
*/
function minMoves(nums: number[]): number {
    let maxVal: number = 0;
    for (const num of nums) {
        maxVal = Math.max(maxVal, num);
    }
    let res: number = 0;
    for (const num of nums) {
        res += (maxVal - num);
    }
    return res;
};
