# You are given a binary string s. You are allowed to perform two types of operations on the string in any sequence:
# Type-1: Remove the character at the start of the string s and append it to the end of the string.
# Type-2: Pick any character in s and flip its value, i.e., if its value is '0' it becomes '1' and vice-versa.
# Return the minimum number of type-2 operations you need to perform such that s becomes alternating.
# The string is called alternating if no two adjacent characters are equal.
# For example, the strings "010" and "1010" are alternating, while the string "0100" is not.
class Solution:
    def minFlips(self, s: str) -> int:
        target = "01"
        cnt = sum(c != target[i & 1] for i, c in enumerate(s))
        ans = min(cnt, len(s) - cnt)
        for i in range(len(s)):
            cnt -= s[i] != target[i & 1]
            cnt += s[i] != target[(i + len(s)) & 1]
            ans = min(ans, cnt, len(s) - cnt)
        return ans
