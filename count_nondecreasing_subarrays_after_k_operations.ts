/*
You are given an array nums of n integers and an integer k.
For each subarray of nums, you can apply up to k operations on it. In each operation, you increment any element of the subarray by 1.
Note that each subarray is considered independently, meaning changes made to one subarray do not persist to another.
Return the number of subarrays that you can make non-decreasing ​​​​​after performing at most k operations.
An array is said to be non-decreasing if each element is greater than or equal to its previous element, if it exists.
*/
function countNonDecreasingSubarrays(nums: number[], k: number): number {
    const n: number = nums.length - 1;
    const deque = new Array<[number, number]>(nums.length);
    let head: number = nums.length;
    let tail: number = nums.length;
    let res: number = 0;
    let cost: number = 0;
    let r: number = n;
    for (let l: number = n; l >= 0; --l) {
        const x: number = nums[l];
        let count: number = 1;
        while (head < tail && deque[head][0] <= x) {
            const [val, cnt]: [number, number] = deque[head++];
            cost += (x - val) * cnt;
            count += cnt;
        }
        deque[--head] = [x, count];
        while (cost > k) {
            const backBlock: [number, number] = deque[tail - 1];
            cost -= backBlock[0] - nums[r];
            --backBlock[1];
            if (backBlock[1] === 0) {
                --tail;
            }
            --r;
        }
        res += r - l + 1;
    }
    return res; 
};
