# letter i reverts the string

class Solution:
    def finalString(self, s: str) -> str:
        res = ""
        for symb in s:
            if symb == "i":
                res = res[::-1]
            else:
                res += symb
        return res
