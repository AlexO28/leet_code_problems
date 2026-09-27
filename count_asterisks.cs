/*
You are given a string s, where every two consecutive vertical bars '|' are grouped into a pair. In other words, the 1st and 2nd '|' make a pair, the 3rd and 4th '|' make a pair, and so forth.
Return the number of '*' in s, excluding the '*' between each pair of '|'.
Note that each '|' will belong to exactly one pair.
*/
public class Solution {
    public int CountAsterisks(string s) {
        bool canCount = true;
        int res = 0;
        foreach (char elem in s) {
            if (elem == '*') {
                if (canCount) {
                    ++res;
                }
            } else if (elem == '|') {
                if (canCount) {
                    canCount = false;
                } else {
                    canCount = true;
                }
            }
        }
        return res;
    }
}
