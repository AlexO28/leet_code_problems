/*
You are given an array of strings ideas that represents a list of names to be used in the process of naming a company. The process of naming a company is as follows:
Choose 2 distinct names from ideas, call them ideaA and ideaB.
Swap the first letters of ideaA and ideaB with each other.
If both of the new names are not found in the original ideas, then the name ideaA ideaB (the concatenation of ideaA and ideaB, separated by a space) is a valid company name.
Otherwise, it is not a valid name.
Return the number of distinct valid names for the company.
*/
using System.Collections.Generic;


public class Solution {
    public long DistinctNames(string[] ideas) {
        ISet<string> s = new HashSet<string>();
        foreach (string idea in ideas) {
            s.Add(idea);
        }
        int[,] f = new int[26, 26];
        foreach (string idea in ideas) {
            char[] t = idea.ToCharArray();
            int i = t[0] - 'a';
            for (int j = 0; j < 26; ++j) {
                t[0] = (char)(j + 'a');
                if (!s.Contains(new string(t))) {
                    ++f[i, j];
                }
            }
        }
        long res = 0;
        foreach (string idea in ideas) {
            char[] t = idea.ToCharArray();
            int i = t[0] - 'a';
            for (int j = 0; j < 26; ++j) {
                t[0] = (char)(j + 'a');
                if (!s.Contains(new string(t))) {
                    res += f[j, i];
                }
            }
        }
        return res;
    }
}
