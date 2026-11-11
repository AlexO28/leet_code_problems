/*
Given an integer array nums of positive integers, return the average value of all even integers that are divisible by 3.
Note that the average of n elements is the sum of the n elements divided by n and rounded down to the nearest integer.
*/
function averageValue(nums: number[]): number {
    let sum: number = 0;
    let count: number = 0;
    for (const num of nums) {
        if (num % 6 == 0) {
            sum += num;
            ++count;
        }
    }
    if (count > 0) {
        sum = Math.floor(sum/count);
    }
    return sum;
};
