/*
You are given an integer array nums and two integers, x and k. You can perform the following operation any number of times (including zero):
Increase or decrease any element of nums by 1.
Return the minimum number of operations needed to have at least k non-overlapping subarrays of size exactly x in nums, where all elements within each subarray are equal.
*/
const INF: bigint = 4611686018427387903n;

function minOperations(nums: number[], x: number, k: number): number {
    const n: number = nums.length;
    
    if (k * x > n) {
        return -1;
    }

    const minOps: bigint[] = getMinOps(nums, x);

    const dp: bigint[][] = Array.from({ length: n + 1 }, () => new Array<bigint>(k + 1).fill(INF));
    for (let i: number = 0; i <= n; ++i) {
        dp[i][0] = 0n;
    }

    for (let i: number = n - 1; i >= 0; --i) {
        for (let j: number = 1; j <= k; ++j) {
            let res: bigint = dp[i + 1][j];
            if (i + x <= n && minOps[i] !== undefined) {
                const prev: bigint = dp[i + x][j - 1];
                if (prev !== INF) {
                    const cost: bigint = minOps[i] + prev;
                    if (cost < res) {
                        res = cost;
                    }
                }
            }
            dp[i][j] = res;
        }
    }
    return dp[0][k] >= INF ? -1 : Number(dp[0][k]);
}

function getMinOps(nums: number[], x: number): bigint[] {
    const n: number = nums.length;
    const minOps: bigint[] = new Array<bigint>(n);
    const finder: WindowMedianTracker = new WindowMedianTracker();
    for (let i: number = 0; i < n; ++i) {
        finder.addNum(nums[i]);
        if (i >= x) {
            finder.removeNum(nums[i - x]);
        }
        if (i >= x - 1) {
            const median: bigint = finder.getMedian();
            const ops: bigint = (median * BigInt(finder.leftSize) - finder.leftSum) + 
                        (finder.rightSum - median * BigInt(finder.rightSize));
            minOps[i - x + 1] = ops;
        }
    }
    return minOps;
}

class MinMaxHeap<T> {
    private data: T[] = [];
    constructor(private compare: (a: T, b: T) => number) {}

    public push(val: T): void {
        this.data.push(val);
        this.up(this.data.length - 1);
    }

    public pop(): T | undefined {
        if (this.data.length === 0) {
            return undefined;
        }
        const top: T = this.data[0];
        const bottom: T | undefined = this.data.pop();
        if (this.data.length > 0 && bottom !== undefined) {
            this.data[0] = bottom;
            this.down(0);
        }
        return top;
    }

    public peek(): T | undefined {
        if (this.data.length === 0) {
            return undefined;
        }
        return this.data[0];
    }

    public get size(): number {
        return this.data.length;
    }

    private up(i: number): void {
        while (i > 0) {
            const p: number = (i - 1) >> 1;
            if (this.compare(this.data[i], this.data[p]) < 0) {
                const temp: T = this.data[i];
                this.data[i] = this.data[p];
                this.data[p] = temp;
                i = p;
            } else {
                break;
            }
        }
    }

    private down(i: number): void {
        const len: number = this.data.length;
        while ((i << 1) + 1 < len) {
            let left: number = (i << 1) + 1;
            let right: number = left + 1;
            let best: number = left;
            if (right < len && this.compare(this.data[right], this.data[left]) < 0) {
                best = right;
            }
            if (this.compare(this.data[best], this.data[i]) < 0) {
                const temp: T = this.data[i];
                this.data[i] = this.data[best];
                this.data[best] = temp;
                i = best;
            } else {
                break;
            }
        }
    }
}

class WindowMedianTracker {
    private leftHeap: MinMaxHeap<number> = new MinMaxHeap<number>((a: number, b: number) => b - a);
    private rightHeap: MinMaxHeap<number> = new MinMaxHeap<number>((a: number, b: number) => a - b);
    private leftDelayed: Map<number, number> = new Map<number, number>();
    private rightDelayed: Map<number, number> = new Map<number, number>();

    public leftSize: number = 0;
    public rightSize: number = 0;
    public leftSum: bigint = 0n;
    public rightSum: bigint = 0n;

    private pruneLeft(): void {
        while (this.leftHeap.size > 0) {
            const top: number = this.leftHeap.peek()!;
            const count: number = this.leftDelayed.get(top) ?? 0;
            if (count > 0) {
                if (count === 1) {
                    this.leftDelayed.delete(top);
                } else {
                    this.leftDelayed.set(top, count - 1);
                }
                this.leftHeap.pop();
            } else {
                break;
            }
        }
    }

    private pruneRight(): void {
        while (this.rightHeap.size > 0) {
            const top: number = this.rightHeap.peek()!;
            const count: number = this.rightDelayed.get(top) ?? 0;
            if (count > 0) {
                if (count === 1) {
                    this.rightDelayed.delete(top);
                } else {
                    this.rightDelayed.set(top, count - 1);
                }
                this.rightHeap.pop();
            } else {
                break;
            }
        }
    }

    private balance(): void {
        if (this.leftSize < this.rightSize) {
            this.pruneRight();
            const val: number = this.rightHeap.pop()!;
            --this.rightSize;
            this.rightSum -= BigInt(val);
            this.leftHeap.push(val);
            ++this.leftSize;
            this.leftSum += BigInt(val);
        } else if (this.leftSize - this.rightSize > 1) {
            this.pruneLeft();
            const val: number = this.leftHeap.pop()!;
            --this.leftSize;
            this.leftSum -= BigInt(val);
            this.rightHeap.push(val);
            ++this.rightSize;
            this.rightSum += BigInt(val);
        }
    }

    public addNum(num: number): void {
        this.pruneLeft();
        if (this.leftSize === 0 || num <= this.leftHeap.peek()!) {
            this.leftHeap.push(num);
            ++this.leftSize;
            this.leftSum += BigInt(num);
        } else {
            this.rightHeap.push(num);
            ++this.rightSize;
            this.rightSum += BigInt(num);
        }
        this.balance();
    }

    public removeNum(num: number): void {
        this.pruneLeft();
        if (this.leftHeap.size > 0 && num <= this.leftHeap.peek()!) {
            this.leftDelayed.set(num, (this.leftDelayed.get(num) ?? 0) + 1);
            --this.leftSize;
            this.leftSum -= BigInt(num);
        } else {
            this.rightDelayed.set(num, (this.rightDelayed.get(num) ?? 0) + 1);
            --this.rightSize;
            this.rightSum -= BigInt(num);
        }
        this.balance();
    }

    public getMedian(): bigint {
        this.pruneLeft();
        return BigInt(this.leftHeap.peek()!);
    }
}
