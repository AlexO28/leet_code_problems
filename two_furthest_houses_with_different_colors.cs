/* There are n houses evenly lined up on the street, and each house is beautifully painted. You are given a 0-indexed integer array colors of length n, where colors[i] represents the color of the ith house.
Return the maximum distance between two houses with different colors.
The distance between the ith and jth houses is abs(i - j), where abs(x) is the absolute value of x.
*/
using System;


public class Solution {
    public int MaxDistance(int[] colors) {
        int maxDist = 0;
        for (int i = 0; i < colors.Length; ++i) {
            if (colors[i] != colors[0]) {
                maxDist = Math.Max(maxDist, i);
            }
            if (colors[i] != colors[^1]) {
                maxDist = Math.Max(maxDist, colors.Length - i - 1);
            }
        }
        return maxDist;        
    }
}
