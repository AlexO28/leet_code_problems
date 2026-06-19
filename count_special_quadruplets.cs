/*Given a 0-indexed integer array nums, return the number of distinct quadruplets (a, b, c, d) such that:
nums[a] + nums[b] + nums[c] == nums[d], and
a < b < c < d*/
public class Solution {
    public int CountQuadruplets(int[] nums) {
        int numberOfQuadruplets = 0;
        for (int a = 0; a < nums.Length; ++a) {
            for (int b = a + 1; b < nums.Length; ++b) {
                for (int c = b + 1; c < nums.Length; ++c) {
                    for (int d = c + 1; d < nums.Length; ++d) {
                        if (nums[a] + nums[b] + nums[c] == nums[d]) {
                            ++numberOfQuadruplets;
                        }
                    }
                }
            }
        }
        return numberOfQuadruplets;
    }
}
