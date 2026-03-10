# You are given two strings a and b that consist of lowercase letters. In one operation, you can change any character in a or b to any lowercase letter.
# Your goal is to satisfy one of the following three conditions:
# Every letter in a is strictly less than every letter in b in the alphabet.
# Every letter in b is strictly less than every letter in a in the alphabet.
# Both a and b consist of only one distinct letter.
# Return the minimum number of operations needed to achieve your goal.
class Solution:
    def minCharacters(self, a: str, b: str) -> int:
        cnt1 = [0] * 26
        cnt2 = [0] * 26
        for c in a:
            cnt1[ord(c) - ord("a")] += 1
        for c in b:
            cnt2[ord(c) - ord("a")] += 1
        summa = len(a) + len(b)
        self.res = summa
        for c1, c2 in zip(cnt1, cnt2):
            self.res = min(self.res, summa - c1 - c2)
        self.f(cnt1, cnt2)
        self.f(cnt2, cnt1)
        return self.res

    def f(self, cnt1, cnt2):
        for i in range(1, 26):
            t = sum(cnt1[i:]) + sum(cnt2[:i])
            self.res = min(self.res, t)
