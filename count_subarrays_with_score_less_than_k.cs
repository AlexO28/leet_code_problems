/*
The score of an array is defined as the product of its sum and its length.
Given a positive integer array nums and an integer k, return the number of non-empty subarrays of nums whose score is strictly less than k.
A subarray is a contiguous sequence of elements within an array.
*/
public class Solution {
    public long CountSubarrays(int[] nums, long k) {
        long res = 0;
        long s = 0;
        for (int i = 0, j = 0; i < nums.Length; ++i) {
            s += nums[i];
            while (s * (i - j + 1) >= k) {
                s -= nums[j++];
            }
            res += i - j + 1;
        }
        return res;
    }
}
