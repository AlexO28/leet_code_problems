/* Given a string s and a character letter, return the percentage of characters in s that equal letter rounded down to the nearest whole percent. */
public class Solution {
    public int PercentageLetter(string s, char letter) {
        int num = 0;
        foreach (char elem in s) {
            if (elem == letter) {
                ++num;
            }
        }
        return (100 * num) / s.Length;
    }
}
