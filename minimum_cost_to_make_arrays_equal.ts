/*
You are given two 0-indexed arrays nums and cost consisting each of n positive integers.
You can do the following operation any number of times:
Increase or decrease any element of the array nums by 1.
The cost of doing one operation on the ith element is cost[i].
Return the minimum total cost such that all the elements of the array nums become equal.
*/
function minCost(nums: number[], cost: number[]): number {
    const arr: [number, number][] = nums.map((num, i) => [num, cost[i]]);
    arr.sort((a, b) => a[0] - b[0]);
    const n: number = nums.length + 1;
    const f: BigInt64Array = new BigInt64Array(n).fill(0n);
    const g: BigInt64Array = new BigInt64Array(n).fill(0n);
    for (let i: number = 1; i < n; ++i) {
        const a: bigint = BigInt(arr[i - 1][0]);
        const b: bigint = BigInt(arr[i - 1][1]);
        f[i] = f[i - 1] + a * b;
        g[i] = g[i - 1] + b;
    }
    let res: bigint = 9223372036854775807n;
    for (let i: number = 1; i < n; ++i) {
        const a: bigint = BigInt(arr[i - 1][0]);
        const l: bigint = a * g[i - 1] - f[i - 1];
        const r: bigint = f[nums.length] - f[i] - a * (g[nums.length] - g[i]);
        const cursum: bigint = l + r;
        if (res > cursum) {
            res = cursum;
        }
    }
    return Number(res);
};
