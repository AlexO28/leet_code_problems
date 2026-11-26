/*
Given an integer num, return the number of digits in num that divide num.
An integer val divides nums if nums % val == 0.
*/
public class Solution {
    public int CountDigits(int num) {
        string numStr = num.ToString();
        int count = 0;
        for (int j = 0; j < numStr.Length; ++j) {
            if (numStr[j] != '0') {
                int val = numStr[j] - '0';
                if (num % val == 0) {
                    ++count;
                }
            }
        }
        return count;
    }
}
