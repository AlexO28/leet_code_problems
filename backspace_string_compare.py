# Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.
# Note that after backspacing an empty text, the text will continue empty.


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s = list(s)
        t = list(t)
        return self.decode(s) == self.decode(t)

    def decode(self, s):
        res = []
        for elem in s:
            if elem == "#":
                if len(res) > 0:
                    res.pop()
            else:
                res.append(elem)
        return res
