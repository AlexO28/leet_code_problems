# You are given a string s and array queries where queries[i] = [lefti, righti, ki]. We may rearrange the substring s[lefti...righti] for each query and then choose up to ki of them to replace with any lowercase English letter.
# If the substring is possible to be a palindrome string after the operations above, the result of the query is true. Otherwise, the result is false.
# Return a boolean array answer where answer[i] is the result of the ith query queries[i].
# Note that each letter is counted individually for replacement, so if, for example s[lefti...righti] = "aaa", and ki = 2, we can only replace two of the letters. Also, note that no query modifies the initial string s.
from typing import List


class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        prefix_sum = [[0] * 26 for i in range(len(s) + 1)]
        a_code = ord("a")
        for index, char in enumerate(s, 1):
            prefix_sum[index] = prefix_sum[index-1].copy()
            prefix_sum[index][ord(char) - a_code] += 1
        res = []
        for start, end, max_replacements in queries:
            res.append(sum((prefix_sum[end + 1][j] - prefix_sum[start][j]) & 1 for j in range(26)) // 2 <= max_replacements)
        return res
