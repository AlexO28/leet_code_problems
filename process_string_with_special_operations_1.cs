# You are given a string s consisting of lowercase English letters and the special characters: *, #, and %.
# Build a new string result by processing s according to the following rules from left to right:
# If the letter is a lowercase English letter append it to result.
# A '*' removes the last character from result, if it exists.
# A '#' duplicates the current result and appends it to itself.
# A '%' reverses the current result.
# Return the final string result after processing all characters in s.
using System.Text;


public class Solution {
    public string ProcessStr(string s) {
        StringBuilder sb = new StringBuilder();
        foreach (char elem in s) {
            if (elem == '*') {
                if (sb.Length > 0) {
                    --sb.Length;
                }
            } else if (elem == '#') {
                char[] buffer = new char[sb.Length];
                sb.CopyTo(0, buffer, 0, sb.Length);
                sb.Append(buffer);
            } else if (elem == '%') {
                int left = 0;
                int right = sb.Length - 1;
                while (left < right) {
                    char temp = sb[left];
                    sb[left] = sb[right];
                    sb[right] = temp;
                    ++left;
                    --right;
                }
            } else {
                sb.Append(elem);
            }
        }
        return sb.ToString();
    }
}
