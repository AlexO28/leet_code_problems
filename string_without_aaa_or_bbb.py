# Given two integers a and b, return any string s such that:
# s has length a + b and contains exactly a 'a' letters, and exactly b 'b' letters,
# The substring 'aaa' does not occur in s, and
# The substring 'bbb' does not occur in s.
class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        res = []
        while (a > 0) and (b > 0):
            if a > b:
                res.append("aab")
                a -= 2
                b -= 1
            elif a < b:
                res.append("bba")
                b -= 2
                a -= 1
            else:
                res.append("ab")
                a -= 1
                b -= 1
        if a > 0:
            res.append("a"*a)
        elif b > 0:
            res.append("b"*b)
        return "".join(res)
