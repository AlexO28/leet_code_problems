/*
You are given an undirected tree with n nodes labeled 0 to n - 1. This is represented by a 2D array edges of length n - 1, where edges[i] = [ui, vi] indicates an undirected edge between nodes ui and vi.
You are also given a string s of length n consisting of lowercase English letters, where s[i] represents the character assigned to node i.
You are also given a string array queries, where each queries[i] is either:
"update ui c": Change the character at node ui to c. Formally, update s[ui] = c.
"query ui vi": Determine whether the string formed by the characters on the unique path from ui to vi (inclusive) can be rearranged into a palindrome.
Return a boolean array answer, where answer[j] is true if the jth query of type "query ui vi"​​​​​​​ can be rearranged into a palindrome, and false otherwise.
*/
function palindromePath(n: number, edges: number[][], s: string, queries: string[]): boolean[] {
    const LOG: number = Math.floor(Math.log2(n)) + 1;
    const adj: number[][] = Array.from({ length: n }, () => []);
    for (const [u, v] of edges) {
        adj[u].push(v);
        adj[v].push(u);
    }
    const timeIn: Int32Array = new Int32Array(n);
    const timeOut: Int32Array = new Int32Array(n);
    const timerRef = { val: 0 };    
    const up: Int32Array[] = Array.from({ length: n }, () => new Int32Array(LOG));
    const currentMasks: Int32Array = new Int32Array(n);
    const nodeCharBit: Int32Array = new Int32Array(n);
    const ACODE: number = 'a'.charCodeAt(0);
    for (let i: number = 0; i < n; ++i) {
        nodeCharBit[i] = 1 << (s.charCodeAt(i) - ACODE);
    }
    search(0, 0, 0, timeIn, timerRef, up, currentMasks, nodeCharBit, adj, timeOut, LOG);
    const bit: Int32Array = new Int32Array(timerRef.val + 2);
    for (let i: number = 0; i < n; ++i) {
        bitUpdate(timeIn[i], currentMasks[i], timerRef.val, bit);
        bitUpdate(timeIn[i] + 1, currentMasks[i], timerRef.val, bit);
    }
    const res: boolean[] = [];
    for (const query of queries) {
        const parts: string[] = query.split(" ");
        if (parts[0] === "update") {
            const node: number = parseInt(parts[1], 10);
            const newChar: string = parts[2];
            const newBit: number = 1 << (newChar.charCodeAt(0) - ACODE);
            const oldBit: number = nodeCharBit[node];
            if (oldBit !== newBit) {
                const change: number = oldBit ^ newBit;
                nodeCharBit[node] = newBit;
                bitUpdate(timeIn[node], change, timerRef.val, bit);
                bitUpdate(timeOut[node] + 1, change, timerRef.val, bit);
            }
        } else {
            const u: number = parseInt(parts[1], 10);
            const v: number = parseInt(parts[2], 10);    
            const maskU: number = bitQuery(timeIn[u], bit);
            const maskV: number = bitQuery(timeIn[v], bit);
            const lca: number = getLca(u, v, timeIn, timeOut, up, LOG);
            const lcaCharBit: number = nodeCharBit[lca];    
            const pathMask: number = maskU ^ maskV ^ lcaCharBit;
            res.push((pathMask & (pathMask - 1)) === 0);
        }
    }
    return res;
}

function search(
    u: number, 
    p: number, 
    currentXor: number, 
    timeIn: Int32Array, 
    timerRef: { val: number }, 
    up: Int32Array[], 
    currentMasks: Int32Array, 
    nodeCharBit: Int32Array,
    adj: number[][], 
    timeOut: Int32Array, 
    LOG: number
): void {
    timeIn[u] = ++timerRef.val;
    up[u][0] = p;
    for (let i: number = 1; i < LOG; ++i) {
        up[u][i] = up[up[u][i - 1]][i - 1];
    }        
    currentMasks[u] = currentXor ^ nodeCharBit[u];
    for (const v of adj[u]) {
        if (v !== p) {
            search(v, u, currentMasks[u], timeIn, timerRef, up, currentMasks, nodeCharBit, adj, timeOut, LOG);
        }
    }
    timeOut[u] = timerRef.val;
}

function bitUpdate(idx: number, val: number, timer: number, bit: Int32Array): void {
    for (; idx <= timer; idx += idx & -idx) {
        bit[idx] ^= val;
    }
}

function bitQuery(idx: number, bit: Int32Array): number {
    let sum: number = 0;
    for (; idx > 0; idx -= idx & -idx) {
        sum ^= bit[idx];
    }
    return sum;
}

function getLca(
    u: number, 
    v: number, 
    timeIn: Int32Array,
    timeOut: Int32Array,
    up: Int32Array[],
    LOG: number
): number {
    if (isAncestor(u, v, timeIn, timeOut)) {
        return u;
    }
    if (isAncestor(v, u, timeIn, timeOut)) {
        return v;
    }
    for (let i: number = LOG - 1; i >= 0; --i) {
        if (!isAncestor(up[u][i], v, timeIn, timeOut)) {
            u = up[u][i];
        }
    }
    return up[u][0];
}

function isAncestor(
    u: number, 
    v: number, 
    timeIn: Int32Array,
    timeOut: Int32Array
): boolean {
    return timeIn[u] <= timeIn[v] && timeOut[u] >= timeOut[v];
}
