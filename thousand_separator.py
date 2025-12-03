# Given an integer n, add a dot (".") as the thousands separator and return it in string format.
class Solution:
    def thousandSeparator(self, n: int) -> str:
        n = list(str(n))
        res = []
        for i in range(1, len(n) + 1):
            if (i > 1) and (i % 3 == 1):
                res.append(".")
            res.append(str(n[-i]))
        return "".join(res[::-1])
