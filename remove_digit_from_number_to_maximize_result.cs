/*
You are given a string number representing a positive integer and a character digit.
Return the resulting string after removing exactly one occurrence of digit from number such that the value of the resulting string in decimal form is maximized. The test cases are generated such that digit occurs at least once in number.
*/
using System.Numerics;


public class Solution {
    public string RemoveDigit(string number, char digit) {
        string finalCandidate = "";
        string candidate;
        BigInteger res = -1;
        for (int i = 0; i < number.Length; ++i) {
            if (number[i] == digit) {
                if (i == 0) {
                    candidate = number[1..];
                } else if (i == number.Length - 1) {
                    candidate = number[..i];
                } else {
                    candidate = number[..i] + number[(i + 1)..];
                }
                BigInteger num = BigInteger.Parse(candidate);
                if (num > res) {
                    res = num;
                    finalCandidate = candidate;
                }
            }
        }
        return finalCandidate;
    }
}
