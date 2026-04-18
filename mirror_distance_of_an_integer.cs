/* You are given an integer n.
Define its mirror distance as: abs(n - reverse(n))​​​​​​​ where reverse(n) is the integer formed by reversing the digits of n.
Return an integer denoting the mirror distance of n​​​​​​​.
abs(x) denotes the absolute value of x.*/
using System;
using System.Linq;


public class Solution {
    public int MirrorDistance(int n) {
        string reversed = new string(n.ToString().Reverse().ToArray());
        return Math.Abs(n - int.Parse(reversed));
    }
}
