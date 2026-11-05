# You are given a string s and a robot that currently holds an empty string t. Apply one of the following operations until s and t are both empty:
# Remove the first character of a string s and give it to the robot. The robot will append this character to the string t.
# Remove the last character of a string t and give it to the robot. The robot will write this character on paper.
# Return the lexicographically smallest string that can be written on the paper.
from collections import Counter


class Solution:
    def robotWithString(self, s: str) -> str:
        cnt = Counter(s)
        res = []
        stk = []
        elem = "a"
        for c in s:
            cnt[c] -= 1
            while elem < "z" and cnt[elem] == 0:
                elem = chr(ord(elem) + 1)
            stk.append(c)
            while stk and stk[-1] <= elem:
                res.append(stk.pop())
        return "".join(res)
