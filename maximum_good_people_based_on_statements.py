# There are two types of persons:
# The good person: The person who always tells the truth.
# The bad person: The person who might tell the truth and might lie.
# You are given a 0-indexed 2D integer array statements of size n x n that represents the statements made by n people about each other. More specifically, statements[i][j] could be one of the following:
# 0 which represents a statement made by person i that person j is a bad person.
# 1 which represents a statement made by person i that person j is a good person.
# 2 represents that no statement is made by person i about person j.
# Additionally, no person ever makes a statement about themselves. Formally, we have that statements[i][i] = 2 for all 0 <= i < n.
# Return the maximum number of people who can be good based on the statements made by the n people.
from typing import List


class Solution:
    def maximumGood(self, statements: List[List[int]]) -> int:
        self.statements = statements
        return max(self.check(i) for i in range(1, 1 << len(self.statements)))

    def check(self, mask):
        cnt = 0
        for i, row in enumerate(self.statements):
            if mask >> i & 1:
                for j, x in enumerate(row):
                    if x < 2 and (mask >> j & 1) != x:
                        return 0
                cnt += 1
        return cnt
