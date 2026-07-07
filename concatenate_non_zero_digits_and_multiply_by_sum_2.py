# You are given a string s of length m consisting of digits. You are also given a 2D integer array queries, where queries[i] = [li, ri].
# For each queries[i], extract the substring s[li..ri]. Then, perform the following:
# Form a new integer x by concatenating all the non-zero digits from the substring in their original order. If there are no non-zero digits, x = 0.
# Let sum be the sum of digits in x. The answer is x * sum.
# Return an array of integers answer where answer[i] is the answer to the ith query.
# Since the answers may be very large, return them modulo 109 + 7.
from typing import List


class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 1000000007
        pow10 = [0] * (len(s) + 1)
        pow10[0] = 1
        idx = [0] * (len(s) + 1)
        x = [0] * (len(s) + 1)
        total = [0] * (len(s) + 1)
        for i in range(len(s)):
            d = ord(s[i]) - ord("0")
            pow10[i + 1] = (pow10[i] * 10) % MOD
            idx[i + 1] = idx[i] + (1 if d else 0)
            x[i + 1] = (x[i] * 10 + d) % MOD if d else x[i]
            total[i + 1] = total[i] + d
        return [
            (
                ((x[r + 1] - x[l] * pow10[idx[r + 1] - idx[l]]) % MOD)
                * (total[r + 1] - total[l])
            )
            % MOD
            for l, r in queries
        ]
