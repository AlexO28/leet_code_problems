# Given a string s, return the number of different non-empty palindromic subsequences in s. Since the answer may be very large, return it modulo 109 + 7.
# A subsequence of a string is obtained by deleting zero or more characters from the string.
# A sequence is palindromic if it is equal to the sequence reversed.
class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        MOD = 10**9 + 7
        ord_dict = {'a': 0,
                    'b': ord('b')-ord('a'),
                    'c': ord('c')-ord('a'),
                    'd': ord('d')-ord('a')}
        dp = [[[0] * 4 for _ in range(len(s))] for _ in range(len(s))]
        for j in range(len(s)):
            dp[j][j][ord_dict[s[j]]] = 1
        for sub_len in range(2, len(s)+1):
            for start in range(len(s)-sub_len+1):
                end = start+sub_len-1
                for char in ord_dict.keys():
                    char_index = ord_dict[char]
                    if (s[start] == s[end]) and (s[start] == char):
                        dp[start][end][char_index] = (2 + sum(dp[start + 1][end - 1])) % MOD
                    elif s[start] == char:
                        dp[start][end][char_index] = dp[start][end - 1][char_index]
                    elif s[end] == char:
                        dp[start][end][char_index] = dp[start+1][end][char_index]
                    else:
                        dp[start][end][char_index] = dp[start+1][end-1][char_index]
        return sum(dp[0][len(s)-1]) % MOD
