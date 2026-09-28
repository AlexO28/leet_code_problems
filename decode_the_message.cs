/*
You are given the strings key and message, which represent a cipher key and a secret message, respectively. The steps to decode message are as follows:
Use the first appearance of all 26 lowercase English letters in key as the order of the substitution table.
Align the substitution table with the regular English alphabet.
Each letter in message is then substituted using the table.
Spaces ' ' are transformed to themselves.
For example, given key = "happy boy" (actual key would have at least one instance of each letter in the alphabet), we have the partial substitution table of ('h' -> 'a', 'a' -> 'b', 'p' -> 'c', 'y' -> 'd', 'b' -> 'e', 'o' -> 'f').
Return the decoded message.
*/
using System.Collections.Generic;
using System.Text;


public class Solution {
    public string DecodeMessage(string key, string message) {
        Dictionary<char, int> info = new Dictionary<char, int>();
        int code = 0;
        foreach (char elem in key) {
            if ((elem != ' ') && (!info.ContainsKey(elem))) {
                info[elem] = code++;
            }
        }
        StringBuilder sb = new StringBuilder();
        foreach (char elem in message) {
           if (elem == ' ') {
               sb.Append(elem);
           } else {
               sb.Append((char)('a' + info[elem]));
           }
        }
        return sb.ToString();
    }
}
