# You are given a string s that contains digits 0-9, addition symbols '+', and multiplication symbols '*' only, representing a valid math expression of single digit numbers (e.g., 3+5*2). This expression was given to n elementary school students. The students were instructed to get the answer of the expression by following this order of operations:
# Compute multiplication, reading from left to right; Then,
# Compute addition, reading from left to right.
# You are given an integer array answers of length n, which are the submitted answers of the students in no particular order. You are asked to grade the answers, by following these rules:
# If an answer equals the correct answer of the expression, this student will be rewarded 5 points;
# Otherwise, if the answer could be interpreted as if the student applied the operators in the wrong order but had correct arithmetic, this student will be rewarded 2 points;
# Otherwise, this student will be rewarded 0 points.
# Return the sum of the points of the students.
from typing import List
from collections import Counter


class Solution:
    def scoreOfStudents(self, s: str, answers: List[int]) -> int:
        x = self.calc(s)
        m = (len(s) + 1) >> 1
        f = [[set() for _ in range(m)] for _ in range(m)]
        for i in range(m):
            f[i][i] = {int(s[i << 1])}
        for i in range(m - 1, -1, -1):
            for j in range(i, m):
                for k in range(i, j):
                    for l in f[i][k]:
                        for r in f[k + 1][j]:
                            if s[k << 1 | 1] == "+" and l + r <= 1000:
                                f[i][j].add(l + r)
                            elif s[k << 1 | 1] == "*" and l * r <= 1000:
                                f[i][j].add(l * r)
        cnt = Counter(answers)
        ans = cnt[x] * 5
        for k, v in cnt.items():
            if k != x and k in f[0][m - 1]:
                ans += v << 1
        return ans

    def calc(self, s):
        res = 0
        pre = int(s[0])
        for i in range(1, len(s), 2):
            if s[i] == "*":
                pre *= int(s[i + 1])
            else:
                res += pre
                pre = int(s[i + 1])
        res += pre
        return res
