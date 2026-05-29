/*You are given an integer array nums.
You replace each element in nums with the sum of its digits.
Return the minimum element in nums after all replacements.*/
using System;


public class Solution {
    public int MinElement(int[] nums) {
        int minSum = 100;
        foreach (int num in nums) {
            string numStr = num.ToString();
            int curSum = 0;
            foreach (char elem in numStr) {
                curSum += (int)char.GetNumericValue(elem);
            }
            minSum = Math.Min(minSum, curSum);
        }
        return minSum;
    }
}
