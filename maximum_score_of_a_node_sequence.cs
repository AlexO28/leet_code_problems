/*
There is an undirected graph with n nodes, numbered from 0 to n - 1.
You are given a 0-indexed integer array scores of length n where scores[i] denotes the score of node i. You are also given a 2D integer array edges where edges[i] = [ai, bi] denotes that there exists an undirected edge connecting nodes ai and bi.
A node sequence is valid if it meets the following conditions:
There is an edge connecting every pair of adjacent nodes in the sequence.
No node appears more than once in the sequence.
The score of a node sequence is defined as the sum of the scores of the nodes in the sequence.
Return the maximum score of a valid node sequence with a length of 4. If no such sequence exists, return -1.
*/
using System.Collections.Generic;


public class Solution {
    public int MaximumScore(int[] scores, int[][] edges) {
        List<int>[] g = new List<int>[scores.Length];
        for (int i = 0; i < g.Length; ++i) {
            g[i] = new List<int>();
        }
        foreach (int[] e in edges) {
            g[e[0]].Add(e[1]);
            g[e[1]].Add(e[0]);
        }
        for (int i = 0; i < g.Length; ++i) {
            g[i].Sort((a, b) => scores[b].CompareTo(scores[a]));
            g[i] = g[i].GetRange(0, Math.Min(3, g[i].Count));
        }
        int ans = -1;
        foreach (int[] e in edges) {
            foreach (int c in g[e[0]]) {
                foreach (int d in g[e[1]]) {
                    if ((c != e[1]) && (c != d) && (e[0] != d)) {
                        ans = Math.Max(ans, scores[e[0]] + scores[e[1]] + scores[c] + scores[d]);
                    }
                }
            }
        }
        return ans;
    }
}
