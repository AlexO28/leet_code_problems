/*
You are given a positive integer n representing the number of nodes in an undirected graph. The nodes are labeled from 1 to n.
You are also given a 2D integer array edges, where edges[i] = [ai, bi] indicates that there is a bidirectional edge between nodes ai and bi. Notice that the given graph may be disconnected.
Divide the nodes of the graph into m groups (1-indexed) such that:
Each node in the graph belongs to exactly one group.
For every pair of nodes in the graph that are connected by an edge [ai, bi], if ai belongs to the group with index x, and bi belongs to the group with index y, then |y - x| = 1.
Return the maximum number of groups (i.e., maximum m) into which you can divide the nodes. Return -1 if it is impossible to group the nodes with the given conditions.
*/
using System;
using System.Collections.Generic;


public class Solution {
    public int MagnificentSets(int n, int[][] edges) {
        List<int>[] g = new List<int>[n];
        for (int k = 0; k < g.Length; ++k) {
            g[k] = new List<int>();
        }
        foreach (int[] e in edges) {
            int a = e[0] - 1;
            int b = e[1] - 1;
            g[a].Add(b);
            g[b].Add(a);
        }
        int[] d = new int[n];
        int[] dist = new int[n];
        for (int i = 0; i < n; ++i) {
            LinkedList<int> q = new LinkedList<int>();
            q.AddLast(i);
            for (int j = 0; j < n; ++j) {
                dist[j] = 0;
            }
            dist[i] = 1;
            int mx = 1;
            int root = i;
            while (q.Count > 0) {
                int a = q.First.Value;
                q.RemoveFirst();
                root = Math.Min(root, a);
                foreach (int b in g[a]) {
                    if (dist[b] == 0) {
                        dist[b] = dist[a] + 1;
                        mx = Math.Max(mx, dist[b]);
                        q.AddLast(b);
                    } else if (Math.Abs(dist[b] - dist[a]) != 1) {
                        return -1;
                    }
                }
            }
            d[root] = Math.Max(d[root], mx);
        }
        return d.Sum();
    }
}
