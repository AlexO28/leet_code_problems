/*
There is an undirected connected tree with n nodes labeled from 0 to n - 1 and n - 1 edges.
You are given a 0-indexed integer array nums of length n where nums[i] represents the value of the ith node. You are also given a 2D integer array edges of length n - 1 where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree.
Remove two distinct edges of the tree to form three connected components. For a pair of removed edges, the following steps are defined:
Get the XOR of all the values of the nodes for each of the three components respectively.
The difference between the largest XOR value and the smallest XOR value is the score of the pair.
Return the minimum score of any possible pair of edge removals on the given tree.
*/
using System;
using System.Collections.Generic;


public class Solution {
    private int[] nums;
    private List<int>[] g;
    private int ans = int.MaxValue;
    private int s;
    private int s1;

    public int MinimumScore(int[] nums, int[][] edges) {
        this.nums = nums;
        g = new List<int>[nums.Length];
        for (int i = 0; i < g.Length; i++) {
            g[i] = new List<int>();
        }
        foreach (int[] edge in edges) {
            int a = edge[0];
            int b = edge[1];
            g[a].Add(b);
            g[b].Add(a);
        }
        foreach (int x in nums) {
            s ^= x;
        }
        for (int i = 0; i < nums.Length; ++i) {
            foreach (int j in g[i]) {
                s1 = Search(i, j);
                Search2(i, j);
            }
        }
        return ans;
    }

    private int Search(int i, int ii) {
        int res = nums[i];
        foreach (int j in g[i]) {
            if (j != ii) {
                res ^= Search(j, i);
            }
        }
        return res;
    }

    private int Search2(int i, int ii) {
        int res = nums[i];
        foreach (int j in g[i]) {
            if (j != ii) {
                int s2 = Search2(j, i);
                res ^= s2;
                int max = Math.Max(Math.Max(s ^ s1, s2), s1 ^ s2);
                int min = Math.Min(Math.Min(s ^ s1, s2), s1 ^ s2);
                ans = Math.Min(ans, max - min);
            }
        }
        return res;
    }
}
