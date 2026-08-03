/*
Given two string arrays words1 and words2, return the number of strings that appear exactly once in each of the two arrays.
*/
using System.Collections.Generic;


public class Solution {
    public int CountWords(string[] words1, string[] words2) {
        Dictionary<string, int> stats1 = CalculateStatistics(words1);
        Dictionary<string, int> stats2 = CalculateStatistics(words2);
        int number_of_words = 0;
        foreach (string word in stats1.Keys) {
            if (stats1[word] == 1) {
                if (stats2.ContainsKey(word)) {
                    if (stats2[word] == 1) {
                        ++number_of_words;
                    }
                }
            }
        }
        return number_of_words;
    }

    private Dictionary<string, int> CalculateStatistics(string[] words) {
        Dictionary<string, int> stats = new Dictionary<string, int>();
        foreach (string word in words) {
            if (stats.ContainsKey(word)) {
                stats[word] += 1;
            } else {
                stats[word] = 1;
            }
        }
        return stats;
    }
}
