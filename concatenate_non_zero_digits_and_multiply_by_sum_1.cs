/*
You are given an integer n.
Form a new integer x by concatenating all the non-zero digits of n in their original order. If there are no non-zero digits, x = 0.
Let sum be the sum of digits in x.
Return an integer representing the value of x * sum.
*/
using System.Text;


public class Solution {
    public long SumAndMultiply(int n) {
        if (n == 0) {
            return 0;
        }
        int summa = 0;
        StringBuilder sb = new StringBuilder();
        foreach (char elem in n.ToString()) {
            if (elem != '0') {
               summa += elem - '0';
               sb.Append(elem);
            }
        }
        return long.Parse(sb.ToString()) * summa;
    }
}
