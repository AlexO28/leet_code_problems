/*
You are given an integer array nums.
Return the smallest index i such that the sum of the digits of nums[i] is equal to i.
If no such index exists, return -1.
*/
public class Solution {
    public int SmallestIndex(int[] nums) {
        for (int i = 0; i < nums.Length; ++i) {
            string numStr = nums[i].ToString();
            int diff = i;
            foreach (char digit in numStr) {
                diff -= digit - '0';
                if (diff < 0) {
                    break;
                }
            }
            if (diff == 0) {
                return i;
            }
        }
        return -1;
    }
}
