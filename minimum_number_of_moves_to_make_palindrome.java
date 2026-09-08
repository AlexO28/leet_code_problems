/*
You are given a string s consisting only of lowercase English letters.
In one move, you can select any two adjacent characters of s and swap them.
Return the minimum number of moves needed to make s a palindrome.
Note that the input will be generated such that s can always be converted to a palindrome.
*/
class Solution {
    public int minMovesToMakePalindrome(String s) {
        int ans = 0;
        int n_half = s.length() / 2;
        char[] cs = s.toCharArray();
        for (int i = 0, j = s.length() - 1; i < j; ++i) {
            boolean even = false;
            for (int k = j; k != i; --k) {
                if (cs[i] == cs[k]) {
                    even = true;
                    for (; k < j; ++k) {
                        char t = cs[k];
                        cs[k] = cs[k + 1];
                        cs[k + 1] = t;
                        ++ans;
                    }
                    --j;
                    break;
                }
            }
            if (!even) {
                ans += n_half - i;
            }
        }
        return ans;
    }
}
