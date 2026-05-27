/*
Given a string s, return true if s is a good string, or false otherwise.
A string s is good if all the characters that appear in s have the same number of occurrences (i.e., the same frequency).
*/
using System.Collections.Generic;


public class Solution {
    public bool AreOccurrencesEqual(string s) {
        Dictionary<char, int> frequencies = new();
        int curFrequency = 0;
        foreach (char elem in s) {
            if (frequencies.ContainsKey(elem)) {
                frequencies[elem] += 1;
            } else {
                frequencies.Add(elem, 1);
            }
            curFrequency = frequencies[elem]; 
        }
        foreach (int frequency in frequencies.Values) {
            if (frequency != curFrequency) {
                return false;
            }
        }
        return true;
    }
}
