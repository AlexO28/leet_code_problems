/*
You are given two integers num1 and num2 representing an inclusive range [num1, num2].
The waviness of a number is defined as the total count of its peaks and valleys:
A digit is a peak if it is strictly greater than both of its immediate neighbors.
A digit is a valley if it is strictly less than both of its immediate neighbors.
The first and last digits of a number cannot be peaks or valleys.
Any number with fewer than 3 digits has a waviness of 0.
Return the total sum of waviness for all numbers in the range [num1, num2].
*/
using System;


public class Solution {
    public int TotalWaviness(int num1, int num2) {
        if (num2 < 100) {
            return 0;
        }
        int totalWeaviness = 0;
        for (int num = num1; num <= num2; ++num) {
            string numStr = num.ToString();
            int[] digits = numStr.Select(c => (int)char.GetNumericValue(c)).ToArray();
            int weaviness = 0;
            if (digits.Length > 2) {
                for (int j = 1; j < digits.Length - 1; ++j) {
                    if ((digits[j] > digits[j - 1]) && (digits[j] > digits[j + 1])) {
                        weaviness += 1;
                    } else if ((digits[j] < digits[j - 1]) && (digits[j] < digits[j + 1])) {
                        weaviness += 1;
                    }
                }
            }
            totalWeaviness += weaviness;
        }
        return totalWeaviness;
    }
}
