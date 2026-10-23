/*
Given an integer array nums, return the most frequent even element.
If there is a tie, return the smallest one. If there is no such element, return -1.
*/
using System;
using System.Collections.Generic;
using System.Linq;


public class Solution {
    public int MostFrequentEven(int[] nums) {
        Dictionary<int, int> info = new Dictionary<int, int>();
        int maxVal = -1;
        foreach (int num in nums) {
            if (num % 2 == 0) {
               if (info.ContainsKey(num)) {
                   ++info[num];
               } else {
                   info[num] = 1;
               }
               maxVal = Math.Max(maxVal, info[num]);
            }
        }
        if (maxVal == -1) {
            return -1;
        } else {
            List<int> values = new List<int>();
            foreach (KeyValuePair<int, int> pair in info) {
                if (pair.Value == maxVal) {
                    values.Add(pair.Key);
                }
            }
            return values.Min();
        }
    }
}
