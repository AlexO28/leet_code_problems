/*
Given an array of positive integers nums, return an array answer that consists of the digits of each integer in nums after separating them in the same order they appear in nums.
To separate the digits of an integer is to get all the digits it has in the same order.
For example, for the integer 10921, the separation of its digits is [1,0,9,2,1].
*/
using System.Collections.Generic;


public class Solution {
    public int[] SeparateDigits(int[] nums) {
        List<int> res = new List<int>();
        foreach (int num in nums) {
            string line = num.ToString();
            foreach (char elem in line) {
                res.Add((int)char.GetNumericValue(elem));
            }
        }
        return res.ToArray();
    }
}
