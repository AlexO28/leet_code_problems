/*
You are given a 0-indexed array of strings words. Each string consists of lowercase English letters only. No letter occurs more than once in any string of words.
Two strings s1 and s2 are said to be connected if the set of letters of s2 can be obtained from the set of letters of s1 by any one of the following operations:
Adding exactly one letter to the set of the letters of s1.
Deleting exactly one letter from the set of the letters of s1.
Replacing exactly one letter from the set of the letters of s1 with any letter, including itself.
The array words can be divided into one or more non-intersecting groups. A string belongs to a group if any one of the following is true:
It is connected to at least one other string of the group.
It is the only string present in the group.
Note that the strings in words should be grouped in such a manner that a string belonging to a group cannot be connected to a string present in any other group. It can be proved that such an arrangement is always unique.
Return an array ans of size 2 where:
ans[0] is the maximum number of groups words can be divided into, and
ans[1] is the size of the largest group.
*/
using System.Collections.Generic;


public class Solution {
    private Dictionary<int, int> p;
    private Dictionary<int, int> size;
    private int max;
    private int n;

    public int[] GroupStrings(string[] words) {
        p = new Dictionary<int, int>();
        size = new Dictionary<int, int>();
        n = words.Length;
        max = 0;
        foreach (String word in words) {
            int x = 0;
            foreach (char c in word) {
                x |= 1 << (c - 'a');
            }
            p[x] = x;
            size[x] = size.GetValueOrDefault(x) + 1;
            max = Math.Max(max, size[x]);
            if (size[x] > 1) {
                --n;
            }
        }
        foreach (int x in p.Keys) {
            for (int i = 0; i < 26; ++i) {
                union(x, x ^ (1 << i));
                if (((x >> i) & 1) != 0) {
                    for (int j = 0; j < 26; ++j) {
                        if (((x >> j) & 1) == 0) {
                            union(x, x ^ (1 << i) | (1 << j));
                        }
                    }
                }
            }
        }
        return new int[] {n, max};
    }

    private void union(int a, int b) {
        if (!p.ContainsKey(b)) {
            return;
        }
        int pa = find(a);
        int pb = find(b);
        if (pa == pb) {
            return;
        }
        p[pa] = pb;
        size[pb] += size[pa];
        max = Math.Max(max, size[pb]);
        --n;
    }

    private int find(int x) {
        if (p[x] != x) {
            p[x] = find(p[x]);
        }
        return p[x];
    }
}
