/*
A city is represented as a bi-directional connected graph with n vertices where each vertex is labeled from 1 to n (inclusive). The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself. The time taken to traverse any edge is time minutes.
Each vertex has a traffic signal which changes its color from green to red and vice versa every change minutes. All signals change at the same time. You can enter a vertex at any time, but can leave a vertex only when the signal is green. You cannot wait at a vertex if the signal is green.
The second minimum value is defined as the smallest value strictly larger than the minimum value.
For example the second minimum value of [2, 3, 4] is 3, and the second minimum value of [2, 2, 4] is 4.
Given n, edges, time, and change, return the second minimum time it will take to go from vertex 1 to vertex n.
Notes:
You can go through any vertex any number of times, including 1 and n.
You can assume that when the journey starts, all signals have just turned green.
*/
using System;
using System.Collections.Generic;


public class Solution {
    public int SecondMinimum(int n, int[][] edges, int time, int change) {
        List<int>[] g = new List<int>[n + 1];
        for (int i = 0; i < g.Length; ++i) {
           g[i] = new List<int>();
        }
        foreach (int[] e in edges) {
           int u = e[0];
           int v = e[1];
           g[u].Add(v);
           g[v].Add(u);
        }
        Queue<int[]> q = new Queue<int[]>();
        q.Enqueue(new int[] { 1, 0 });
        int[][] dist = new int[n + 1][];
        for (int i = 0; i <= n; i++) {
           dist[i] = new int[2];
        }
        for (int i = 0; i < n + 1; ++i) {
           dist[i] = new int[2];
           Array.Fill(dist[i], int.MaxValue);
        }
        dist[1][1] = 0;
        while (q.Count > 0) {
            int[] e = q.Dequeue();
            int u = e[0];
            int d = e[1];
            foreach (int v in g[u]) {
                if (d + 1 < dist[v][0]) {
                    dist[v][0] = d + 1;
                    q.Enqueue(new int[] { v, d + 1 });
                } else if (dist[v][0] < d + 1 && d + 1 < dist[v][1]) {
                    dist[v][1] = d + 1;
                    if (v == n) {
                        break;
                    }
                    q.Enqueue(new int[] { v, d + 1 });
                }
            }
        }
        int ans = 0;
        for (int i = 0; i < dist[n][1]; ++i) {
            ans += time;
            if (i < dist[n][1] - 1 && (ans / change) % 2 == 1) {
               ans = (ans + change) / change * change;
            }
        }
        return ans;
    }
}
