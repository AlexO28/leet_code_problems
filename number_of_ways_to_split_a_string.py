# Given a binary string s, you can split s into 3 non-empty strings s1, s2, and s3 where s1 + s2 + s3 = s.
# Return the number of ways s can be split such that the number of ones is the same in s1, s2, and s3. Since the answer may be too large, return it modulo 109 + 7.
class Solution:
    def numWays(self, s: str) -> int:
        s = list(s)
        s = [int(elem) for elem in s]
        main_part, remainder = divmod(sum(s), 3)
        if remainder > 0:
            return 0
        if main_part == 0:
            return int((len(s) - 1) * (len(s) - 2) / 2) % (10**9 + 7)
        num_ones = 0
        i = 0
        while num_ones < main_part:
            if s[i] == 1:
                num_ones += 1
            i += 1
        i -= 1
        j = i + 1
        while s[j] == 0:
            j += 1
        term1 = j - i
        num_ones = 0
        i = len(s) - 1
        while num_ones < main_part:
            if s[i] == 1:
                num_ones += 1
            i -= 1
        i += 1
        j = i - 1
        while s[j] == 0:
            j -= 1
        term2 = i - j
        return (term1 * term2) % (10**9 + 7)
