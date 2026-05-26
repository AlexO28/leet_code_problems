/*
You are given a string word. A letter is called special if it appears both in lowercase and uppercase in word.
Return the number of special letters in word.
*/
using System.Linq;


public class Solution {
    public int NumberOfSpecialChars(string word) {
        string line = string.Concat(word.Distinct());
        int numberOfSpecial = 0;
        foreach (char elem in line) {
            if (char.IsLower(elem)) {
                if (line.Contains(char.ToUpper(elem))) {
                    numberOfSpecial += 1;
                }
            }
        }
        return numberOfSpecial;
    }
}
