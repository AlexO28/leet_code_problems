/*
You are given a 0-indexed string array words.
Two strings are similar if they consist of the same characters.
For example, "abca" and "cba" are similar since both consist of characters 'a', 'b', and 'c'.
However, "abacba" and "bcfd" are not similar since they do not consist of the same characters.
Return the number of pairs (i, j) such that 0 <= i < j <= word.length - 1 and the two strings words[i] and words[j] are similar.
*/
using System.Collections.Generic;


public class Solution {
    public int SimilarPairs(string[] words) {
        if (words.Length == 1) {
            return 0;
        }
        HashSet<char>[] data = new HashSet<char>[words.Length];
        for (int j = 0; j < words.Length; ++j) {
            data[j] = new HashSet<char>(words[j]);
        }
        int res = 0;
        for (int i = 0; i < words.Length - 1; ++i) {
            for (int j = i + 1; j < words.Length; ++j) {
                if (data[i].SetEquals(data[j])) {
                    ++res;
                }
            }
        }
        return res;
    }
}
