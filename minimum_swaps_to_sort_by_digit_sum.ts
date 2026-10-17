/*
You are given an array nums of distinct positive integers. You need to sort the array in increasing order based on the sum of the digits of each number. If two numbers have the same digit sum, the smaller number appears first in the sorted order.
Return the minimum number of swaps required to rearrange nums into this sorted order.
A swap is defined as exchanging the values at two distinct positions in the array.
*/
function minSwaps(nums: number[]): number {
    const arr: [number, number][] = new Array(nums.length);
    for (let i = 0; i < nums.length; ++i) {
        arr[i] = [f(nums[i]), nums[i]];
    }
    arr.sort((a, b) => (a[0] !== b[0] ? a[0] - b[0] : a[1] - b[1]));
    const d = new Map<number, number>();
    for (let i = 0; i < nums.length; ++i) {
        d.set(arr[i][1], i);
    }
    const vis: boolean[] = new Array(nums.length).fill(false);
    let res = nums.length;
    for (let i = 0; i < nums.length; ++i) {
        if (!vis[i]) {
            --res;
            let j = i;
            while (!vis[j]) {
                vis[j] = true;
                j = d.get(nums[j])!;
            }
        }
    }
    return res;   
};

function f(x: number): number {
    let s = 0;
    while (x !== 0) {
        s += x % 10;
        x = Math.floor(x / 10);
    }
    return s;
};
