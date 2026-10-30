/*
You are given an integer n representing the number of nodes in a directed weighted graph, numbered from 0 to n - 1. This is represented by a 2D integer array edges, where edges[i] = [ui, vi, wi] represents a directed edge from node ui to node vi with weight wi.
You are also given a string labels of length n, where labels[i] is the character assigned to node i, and an integer k.
Return the minimum total edge weight of a path from node 0 to node n - 1 such that the concatenation of the labels of the nodes along the path contains at most k consecutive identical characters. If no valid path exists, return -1.
*/
//import { PriorityQueue } from '@datastructures-js/priority-queue';


function shortestPath(n: number, edges: number[][], labels: string, k: number): number {
    const g: [number, number][][] = Array.from({ length: n }, () => []);
    for (const [u, v, w] of edges) {
        g[u].push([v, w]);
    }
    const dist: number[][] = Array.from({ length: n }, () => new Array(k + 1).fill(Infinity));
    dist[0][1] = 0;
    const pq: PriorityQueue<number[]> = new PriorityQueue<number[]>((a, b) => a[0] - b[0]);
    pq.enqueue([0, 0, 1]);
    while (!pq.isEmpty()) {
        const [d, u, cur]: number[] = pq.dequeue();
        if (u === n - 1) {
            return d;
        }
        if (d > dist[u][cur]) {
            continue;
        }
        for (const [v, w] of g[u]) {
            const nxt: number = labels[v] !== labels[u] ? 1 : cur + 1;
            const nd: number = d + w;
            if (nxt <= k && nd < dist[v][nxt]) {
                dist[v][nxt] = nd;
                pq.enqueue([nd, v, nxt]);
            }
        }
    }
    return -1; 
};
