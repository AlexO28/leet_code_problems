/*
You are given a string word. A letter c is called special if it appears both in lowercase and uppercase in word, and every lowercase occurrence of c appears before the first uppercase occurrence of c.
Return the number of special letters in word.
*/
using System;
using System.Collections.Generic;


public class Solution {
    public int NumberOfSpecialChars(string word) {
        Dictionary<char, int> smallLetters = new Dictionary<char, int>();
        Dictionary<char, int> largeLetters = new Dictionary<char, int>();
        for (int j = 0; j < word.Length; ++j) {
            if (char.IsLower(word[j])) {
                if (smallLetters.ContainsKey(word[j])) {
                    smallLetters[word[j]] = j;
                } else {
                    smallLetters.Add(word[j], j);
                }
            } else {
                if (!largeLetters.ContainsKey(Char.ToLower(word[j]))) {
                    largeLetters.Add(Char.ToLower(word[j]), j);
                }
            }
        }
        int numberOfSpecial = 0;
        foreach (var (key, value) in smallLetters) {
            if (largeLetters.ContainsKey(key)) {
                if (largeLetters[key] > smallLetters[key]) {
                    numberOfSpecial += 1;
                }
            }
        }
        return numberOfSpecial;
    }
}
