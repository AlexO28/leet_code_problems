/* Given an array of strings patterns and a string word, return the number of strings in patterns that exist as a substring in word.
A substring is a contiguous sequence of characters within a string. */
public class Solution {
    public int NumOfStrings(string[] patterns, string word) {
        int numberOfStrings = 0;
        foreach (string pattern in patterns) {
            if (word.Contains(pattern)) {
                ++numberOfStrings;
            }
        }
        return numberOfStrings;
    }
}
