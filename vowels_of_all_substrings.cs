/*
Given a string word, return the sum of the number of vowels ('a', 'e', 'i', 'o', and 'u') in every substring of word.
A substring is a contiguous (non-empty) sequence of characters within a string.
Note: Due to the large constraints, the answer may not fit in a signed 32-bit integer. Please be careful during the calculations.
*/
public class Solution {
    public long CountVowels(string word) {
        long summa = 0;
        for (int i = 0; i < word.Length; ++i) {
            if ((word[i] == 'a') || (word[i] == 'e') || (word[i] == 'i') || (word[i] == 'o') || (word[i] == 'u')) {
                summa += (i + 1) * (long)(word.Length - i);
            }
        }
        return summa;
    }
}
