/*
You are given a tree (i.e. a connected, undirected graph that has no cycles) rooted at node 0 consisting of n nodes numbered from 0 to n - 1. The tree is represented by a 0-indexed array parent of size n, where parent[i] is the parent of node i. Since node 0 is the root, parent[0] == -1.
You are also given a string s of length n, where s[i] is the character assigned to node i.
Return the length of the longest path in the tree such that no pair of adjacent nodes on the path have the same character assigned to them.
*/
using System.Collections.Generic;


public class Solution {
    private List<int>[] g;
    private String s;
    private int ans;

    public int LongestPath(int[] parent, string s) {
        g = new List<int>[s.Length];
        this.s = s;
        for (int i = 0; i < g.Length; ++i) {
            g[i] = new List<int>();
        }
        for (int i = 1; i < g.Length; ++i) {
            g[parent[i]].Add(i);
        }
        search(0);
        return ans + 1;
    }

    private int search(int i) {
        int max = 0;
        foreach (int j in g[i]) {
            int x = search(j) + 1;
            if (s[i] != s[j]) {
                ans = Math.Max(ans, max + x);
                max = Math.Max(max, x);
            }
        }
        return max;
    }
}
