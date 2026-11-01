/*
There is a tree (i.e. a connected, undirected graph with no cycles) consisting of n nodes numbered from 0 to n - 1 and exactly n - 1 edges.
You are given a 0-indexed integer array vals of length n where vals[i] denotes the value of the ith node. You are also given a 2D integer array edges where edges[i] = [ai, bi] denotes that there exists an undirected edge connecting nodes ai and bi.
A good path is a simple path that satisfies the following conditions:
The starting node and the ending node have the same value.
All nodes between the starting node and the ending node have values less than or equal to the starting node (i.e. the starting node's value should be the maximum value along the path).
Return the number of distinct good paths.
Note that a path and its reverse are counted as the same path. For example, 0 -> 1 is considered to be the same as 1 -> 0. A single node is also considered as a valid path.
*/
let p: Int32Array;

function numberOfGoodPaths(vals: number[], edges: number[][]): number {
    p = new Int32Array(vals.length);
    const arr: [number, number][] = Array.from({ length: vals.length }, () => [0, 0]);
    const g: number[][] = Array.from({ length: vals.length }, () => []);
    for (const edge of edges) {
        const a: number = edge[0];
        const b: number = edge[1];
        g[a].push(b);
        g[b].push(a);
    }
    const size: Map<number, Map<number, number>> = new Map();
    for (let i: number = 0; i < vals.length; ++i) {
        p[i] = i;
        arr[i] = [vals[i], i];
        if (!size.has(i)) {
            size.set(i, new Map<number, number>());
        }
        size.get(i)!.set(vals[i], 1);
    }
    arr.sort((a, b) => a[0] - b[0]);
    let res: number = vals.length;
    for (const e of arr) {
        const v: number = e[0];
        const a: number = e[1];
        for (const b of g[a]) {
            if (vals[b] <= v) {
                const pa: number = find(a);
                const pb: number = find(b);
                if (pa != pb) {
                    res += (size.get(pa)?.get(v) ?? 0) * (size.get(pb)?.get(v) ?? 0);
                    p[pa] = pb;
                    if (!size.has(pb)) {
                       size.set(pb, new Map());
                    }
                    const sum: number = (size.get(pb)!.get(v) ?? 0) + (size.get(pa)?.get(v) ?? 0);
                    size.get(pb)!.set(v, sum);
                }
            }
        }
    }
    return res;
};

function find(x: number): number {
    if (p[x] != x) {
        p[x] = find(p[x]);
    }
    return p[x];
};
