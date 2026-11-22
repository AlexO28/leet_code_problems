/*
You are given an array nums of size n consisting of distinct integers from 1 to n and a positive integer k.
Return the number of non-empty subarrays in nums that have a median equal to k.
*/
public class Solution {
    public int CountSubarrays(int[] nums, int k) {
        int i = 0;
        while (nums[i] != k) {
            ++i;
        }
        int[] cnt = new int[nums.Length << 1 | 1];
        int res = 1;
        int x = 0;
        for (int j = i + 1; j < nums.Length; ++j) {
            if (nums[j] > k) {
                ++x;
            } else {
                --x;
            }
            if (x >= 0 && x <= 1) {
                ++res;
            }
            ++cnt[x + nums.Length];
        }
        x = 0;
        for (int j = i - 1; j >= 0; --j) {
            if (nums[j] > k) {
                ++x;
            } else {
                --x;
            }
            if (x >= 0 && x <= 1) {
                ++res;
            }
            int delta = -x + nums.Length;
            res += cnt[delta] + cnt[delta + 1];
        }
        return res;
    }
}
