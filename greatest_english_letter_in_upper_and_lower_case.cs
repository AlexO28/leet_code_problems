/*
Given a string of English letters s, return the greatest English letter which occurs as both a lowercase and uppercase letter in s. The returned letter should be in uppercase. If no such letter exists, return an empty string.
An English letter b is greater than another letter a if b appears after a in the English alphabet.
*/
using System.Collections.Generic;


public class Solution {
    public string GreatestLetter(string s) {
        HashSet<char> ss = new HashSet<char>(s);
        for (int i = 0; i < 26; ++i) {
            char letter = (char)('Z' - i);
            if ((ss.Contains(letter)) && (ss.Contains(char.ToLower(letter)))) {
                return letter.ToString();
            }
        }
        return "";
    }
}
