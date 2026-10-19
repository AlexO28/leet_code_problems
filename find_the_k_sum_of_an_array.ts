/*
You are given an integer array nums and a positive integer k. You can choose any subsequence of the array and sum all of its elements together.
We define the K-Sum of the array as the kth largest subsequence sum that can be obtained (not necessarily distinct).
Return the K-Sum of the array.
A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.
Note that the empty subsequence is considered to have a sum of 0.
*/
//import { MinPriorityQueue } from '@datastructures-js/priority-queue';


function kSum(nums: number[], k: number): number {
    let max: number = 0;
    for (let i: number = 0; i < nums.length; ++i) {
        if (nums[i] > 0) {
            max += nums[i];
        } else {
            nums[i] = -nums[i];
        }
    };
    nums.sort((a, b) => a - b);
    const h = new MinPriorityQueue<[number, number]>((pair) => pair[0]);
    h.enqueue([0, 0]);
    for (let i: number = 0; i < k - 1; ++i) {
        let temp = h.dequeue();
        if (temp[1] < nums.length) {
            h.enqueue([temp[0] + nums[temp[1]], temp[1] + 1]);
            if (i > 0) {
                h.enqueue([temp[0] + nums[temp[1]] - nums[temp[1] - 1], temp[1] + 1]);
            };
        };
    };
    return max - h.front()[0];
};
