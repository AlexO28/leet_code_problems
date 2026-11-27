/*
You are given a 2D integer array items, where items[i] = [factori, pricei] represents the ith item. You are also given an integer budget.
There are unlimited copies of each item available for purchase.You may buy any number of copies of any items such that the total cost of the purchased copies is at most budget.
After buying items, you may receive free copies according to the following rules:
For each item i that you bought at least one copy of, you receive one free copy of every item j such that j != i and factori divides factorj.
Buying multiple copies of the same item i does not give additional free copies through item i.
The same item j can be received multiple times for free if it is received from purchases of different item types.
Return the maximum total number of item copies you can obtain, including both purchased copies and free copies, while spending at most budget on purchased items.
*/
using System;


public class Solution {
    public int MaximumSaleItems(int[][] items, int budget) {
        int[] f = new int[budget + 1];
        int mn = int.MaxValue;
        foreach (int[] item in items) {
            mn = Math.Min(mn, item[1]);
            int cnt = 0;
            foreach (int[] jItem in items) {
                if (jItem[0] % item[0] == 0) {
                    ++cnt;
                }
            }
            for (int j = budget; j >= item[1]; --j) {
                f[j] = Math.Max(f[j], f[j - item[1]] + cnt);
            }
        }
        int res = 0;
        for (int i = 0; i <= budget; ++i) {
            res = Math.Max(res, f[i] + (budget - i) / mn);
        }
        return res;
    }
}
