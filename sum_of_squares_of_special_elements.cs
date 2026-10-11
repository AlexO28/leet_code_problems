/*
You are given a 1-indexed integer array nums of length n.
An element nums[i] of nums is called special if i divides n, i.e. n % i == 0.
Return the sum of the squares of all special elements of nums.
*/
public class Solution {
    public int SumOfSquares(int[] nums) {
        int summa = 0;
        for (int i = 0; i < nums.Length; ++i) {
            if (nums.Length % (i + 1) == 0) {
                summa += nums[i] * nums[i];
            }
        }
        return summa;
    }
}
