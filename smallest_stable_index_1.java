/*
You are given an integer array nums of length n and an integer k.
For each index i, define its instability score as max(nums[0..i]) - min(nums[i..n - 1]).
In other words:
max(nums[0..i]) is the largest value among the elements from index 0 to index i.
min(nums[i..n - 1]) is the smallest value among the elements from index i to index n - 1.
An index i is called stable if its instability score is less than or equal to k.
Return the smallest stable index. If no such index exists, return -1.
*/
class Solution {
    public int firstStableIndex(int[] nums, int k) {
        int[] prefixes = new int[nums.length];
        int[] suffixes = new int[nums.length];
        int maxVal = nums[0];
        int minVal = nums[nums.length - 1];
        for (int i = 0; i < nums.length; ++i) {
            maxVal = Math.max(maxVal, nums[i]);
            prefixes[i] = maxVal;
            int ind = nums.length - i - 1;
            minVal = Math.min(minVal, nums[ind]);
            suffixes[ind] = minVal;
        }
        for (int i = 0; i < nums.length; ++i) {
            if (prefixes[i] - suffixes[i] <= k) {
                return i;
            }
        }
        return -1;
    }
}
