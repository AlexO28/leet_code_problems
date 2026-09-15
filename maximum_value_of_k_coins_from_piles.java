/*
There are n piles of coins on a table. Each pile consists of a positive number of coins of assorted denominations.
In one move, you can choose any coin on top of any pile, remove it, and add it to your wallet.
Given a list piles, where piles[i] is a list of integers denoting the composition of the ith pile from top to bottom, and a positive integer k, return the maximum total value of coins you can have in your wallet if you choose exactly k coins optimally.
*/
class Solution {
    public int maxValueOfCoins(List<List<Integer>> piles, int k) {
        int[] f = new int[k + 1];
        for (List<Integer> nums : piles) {
            int[] s = new int[nums.size() + 1];
            for (int j = 1; j <= nums.size(); ++j) {
                s[j] = s[j - 1] + nums.get(j - 1);
            }
            for (int j = k; j >= 0; --j) {
                for (int h = 0; h < s.length && h <= j; ++h) {
                    f[j] = Math.max(f[j], f[j - h] + s[h]);
                }
            }
        }
        return f[k];
    }
}
