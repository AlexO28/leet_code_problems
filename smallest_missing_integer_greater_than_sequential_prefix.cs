/* You are given a 0-indexed array of integers nums.
A prefix nums[0..i] is sequential if, for all 1 <= j <= i, nums[j] = nums[j - 1] + 1. In particular, the prefix consisting only of nums[0] is sequential.
Return the smallest integer x missing from nums such that x is greater than or equal to the sum of the longest sequential prefix. */
using System.Collections.Generic;


public class Solution {
    public int MissingInteger(int[] nums) {
        if (nums.Length == 1) {
            return nums[0] + 1;
        }
        int ind = 0;
        int summa = nums[0];
        while (ind < nums.Length - 1) {
            if (nums[ind + 1] == nums[ind] + 1) {
                summa += nums[++ind];
            } else {
                break;
            }
        }
        HashSet<int> set = new HashSet<int>(nums);
        while (true) {
            if (!set.Contains(summa)) {
                return summa;
            } else {
                ++summa;
            }
        }
    }
}
