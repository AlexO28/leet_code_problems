# Given an integer array queries and a positive integer intLength, return an array answer where answer[i] is either the queries[i]th smallest positive palindrome of length intLength or -1 if no such palindrome exists.
# A palindrome is a number that reads the same backwards and forwards. Palindromes cannot have leading zeros.
from typing import List


class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        l, initmod = divmod(intLength, 2)
        if initmod == 1:
            l += 1
        start = 10 ** (l - 1)
        end = start * 10 - 1
        ans = []
        for q in queries:
            v = start + q - 1
            if v > end:
                ans.append(-1)
            else:
                s = str(v)
                s += s[::-1][initmod:]
                ans.append(int(s))
        return ans
