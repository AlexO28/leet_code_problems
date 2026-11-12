/*
You are given a 0-indexed array of non-negative integers nums. For each integer in nums, you must find its respective second greater integer.
The second greater integer of nums[i] is nums[j] such that:
j > i
nums[j] > nums[i]
There exists exactly one index k such that nums[k] > nums[i] and i < k < j.
If there is no such nums[j], the second greater integer is considered to be -1.
Return an integer array answer, where answer[i] is the second greater integer of nums[i].
*/
function secondGreaterElement(nums: number[]): number[] {
    const secondNextGreater: number[] = new Array(nums.length).fill(-1);
    const stack1: [number, number][] = [];
    const stack2: [number, number][] = [];
    const transporter: [number, number][] = [];
    for (let idx: number = 0; idx < nums.length; ++idx) {
        while (stack2.length > 0 && stack2[stack2.length - 1][0] < nums[idx]) {
            const pastIdx: number = stack2.pop()![1];
            secondNextGreater[pastIdx] = nums[idx];
        }
        while (stack1.length > 0 && stack1[stack1.length - 1][0] < nums[idx]) {
            transporter.push(stack1.pop()!);
        }
        while (transporter.length > 0) {
            stack2.push(transporter.pop()!);
        }
        stack1.push([nums[idx], idx]);
    }
    return secondNextGreater;
};
