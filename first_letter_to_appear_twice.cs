/*
Given a string s consisting of lowercase English letters, return the first letter to appear twice.
Note:
A letter a appears twice before another letter b if the second occurrence of a is before the second occurrence of b.
s will contain at least one letter that appears twice.
*/
using System.Collections.Generic;


public class Solution {
    public char RepeatedCharacter(string s) {
        HashSet<char> set = new HashSet<char>();
        foreach (char elem in s) {
            if (set.Contains(elem)) {
                return elem;
            } else {
                set.Add(elem);
            }
        }
        return ' ';
    }
}
