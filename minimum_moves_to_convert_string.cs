/*
You are given a string s consisting of n characters which are either 'X' or 'O'.
A move is defined as selecting three consecutive characters of s and converting them to 'O'. Note that if a move is applied to the character 'O', it will stay the same.
Return the minimum number of moves required so that all the characters of s are converted to 'O'.
*/
public class Solution {
    public int MinimumMoves(string s) {
        int numberOfMoves = 0;
        char[] newS = s.ToCharArray();
        for (int i = 1; i < newS.Length - 1; ++i) {
            if (newS[i - 1] == 'X') {
                ++numberOfMoves;
                newS[i] = '0';
                newS[i + 1] = '0';
            } else if (i == newS.Length - 2) {
                if ((newS[i] == 'X') || (newS[i + 1] == 'X')) {
                    ++numberOfMoves;
                }
            }
        }
        return numberOfMoves;
    }
}
