/*
You are given a directed graph of n nodes numbered from 0 to n - 1, where each node has at most one outgoing edge.
The graph is represented with a given 0-indexed array edges of size n, indicating that there is a directed edge from node i to node edges[i]. If there is no outgoing edge from i, then edges[i] == -1.
You are also given two integers node1 and node2.
Return the index of the node that can be reached from both node1 and node2, such that the maximum between the distance from node1 to that node, and from node2 to that node is minimized. If there are multiple answers, return the node with the smallest index, and if no possible answer exists, return -1.
Note that edges may contain cycles.
*/
using System;
using System.Collections.Generic;


public class Solution {
    private const int upper = 1073741824;
    private List<int>[] g;

    public int ClosestMeetingNode(int[] edges, int node1, int node2) {
        g = new List<int>[edges.Length];
        for (int i = 0; i < g.Length; ++i) {
            g[i] = new List<int>();
        }
        for (int i = 0; i < edges.Length; ++i) {
            if (edges[i] != -1) {
                g[i].Add(edges[i]);
            }
        }
        int[] d1 = f(node1);
        int[] d2 = f(node2);
        int d = upper;
        int res = -1;
        for (int i = 0; i < edges.Length; ++i) {
            int t = Math.Max(d1[i], d2[i]);
            if (t < d) {
                d = t;
                res = i;
            }
        }
        return res;
    }

    private int[] f(int i) {
        int[] dist = new int[g.Length];
        for (int j = 0; j < dist.Length; ++j) {
            dist[j] = upper;
        }
        dist[i] = 0;
        Queue<int> q = new Queue<int>();
        q.Enqueue(i);
        while (q.Count > 0) {
            i = q.Dequeue();
            foreach (int j in g[i]) {
                if (dist[j] == upper) {
                    dist[j] = dist[i] + 1;
                    q.Enqueue(j);
                }
            }
        }
        return dist;
    }
}
