# As the ruler of a kingdom, you have an army of wizards at your command.
# You are given a 0-indexed integer array strength, where strength[i] denotes the strength of the ith wizard. For a contiguous group of wizards (i.e. the wizards' strengths form a subarray of strength), the total strength is defined as the product of the following two values:
# The strength of the weakest wizard in the group.
# The total of all the individual strengths of the wizards in the group.
# Return the sum of the total strengths of all contiguous groups of wizards. Since the answer may be very large, return it modulo 109 + 7.
# A subarray is a contiguous non-empty sequence of elements within an array.
from itertools import accumulate


class Solution:
    def totalStrength(self, strength: list[int]) -> int:
        left = [-1] * len(strength)
        right = [len(strength)] * len(strength)
        stack = []
        for i, v in enumerate(strength):
            while stack and strength[stack[-1]] >= v:
                stack.pop()
            if stack:
                left[i] = stack[-1]
            stack.append(i)
        stack = []
        for i in range(len(strength) - 1, -1, -1):
            while stack and strength[stack[-1]] > strength[i]:
                stack.pop()
            if stack:
                right[i] = stack[-1]
            stack.append(i)
        ss = list(accumulate(list(accumulate(strength, initial=0)), initial=0))
        MOD = 1000000007
        res = 0
        for i, v in enumerate(strength):
            l, r = left[i] + 1, right[i] - 1
            a = (ss[r + 2] - ss[i + 1]) * (i - l + 1)
            b = (ss[i + 1] - ss[l]) * (r - i + 1)
            res = (res + (a - b) * v) % MOD
        return res
