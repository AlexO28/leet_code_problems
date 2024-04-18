# Given a string s, return the number of palindromic substrings in it.
# A string is a palindrome when it reads the same backward as forward.
# A substring is a contiguous sequence of characters within the string.
class Solution:
    def countSubstrings(self, s: str) -> int:
        if len(s) == 1:
            return 1
        count = 0
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                if s[i:j] == s[i:j][::-1]:
                    count += 1
        return count
