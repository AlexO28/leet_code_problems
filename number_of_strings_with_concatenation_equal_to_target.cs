/*
Given an array of digit strings nums and a digit string target, return the number of pairs of indices (i, j) (where i != j) such that the concatenation of nums[i] + nums[j] equals target.
*/
public class Solution {
    public int NumOfPairs(string[] nums, string target) {
        int res = 0;
        for (int i = 0; i < nums.Length - 1; ++i) {
            for (int j = i + 1; j < nums.Length; ++j) {
                if (nums[i] + nums[j] == target) {
                    ++res;
                }
                if (nums[j] + nums[i] == target) {
                    ++res;
                }
            }
        }
        return res;
    }
}
