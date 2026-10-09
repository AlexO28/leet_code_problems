/*
You are given an integer array nums of length n, and an integer array queries of length m.
Return an array answer of length m where answer[i] is the maximum size of a subsequence that you can take from nums such that the sum of its elements is less than or equal to queries[i].
A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.
*/
using System;


public class Solution {
    public int[] AnswerQueries(int[] nums, int[] queries) {
        Array.Sort(nums);
        int[] res = new int[queries.Length];
        for (int i = 0; i < queries.Length; ++i) {
            int summa = 0;
            foreach (int num in nums) {
                summa += num;
                if (summa <= queries[i]) {
                    ++res[i];
                } else {
                    break;
                }
            }
        }
        return res;
    }
}
