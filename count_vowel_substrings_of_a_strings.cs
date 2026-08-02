/*
A substring is a contiguous (non-empty) sequence of characters within a string.
A vowel substring is a substring that only consists of vowels ('a', 'e', 'i', 'o', and 'u') and has all five vowels present in it.
Given a string word, return the number of vowel substrings in word.
*/
public class Solution {
    public int CountVowelSubstrings(string word) {
        if (word.Length < 5) {
            return 0;
        }
        int number_of_strings = 0;
        for (int i = 0; i < word.Length - 4; ++i) {
            bool has_a = false;
            bool has_e = false;
            bool has_i = false;
            bool has_o = false;
            bool has_u = false;
            for (int j = i; j < word.Length; ++j) {
                if (word[j] == 'a') {
                    has_a = true;
                } else if (word[j] == 'e') {
                    has_e = true;
                } else if (word[j] == 'i') {
                    has_i = true;
                } else if (word[j] == 'o') {
                    has_o = true;
                } else if (word[j] == 'u') {
                    has_u = true;
                } else {
                    break;
                }
                if (has_a && has_e && has_i && has_o && has_u) {
                    ++number_of_strings;
                }
            }
        }
        return number_of_strings;
    }
}
