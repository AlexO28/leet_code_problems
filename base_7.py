# Given an integer num, return a string of its base 7 representation.
class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        if num < 0:
            sign = "-"
        else:
            sign = ""
        num = abs(num)
        res = []
        while True:
            a, b = divmod(num, 7)
            if a == 0:
                res.append(str(b))
                break
            else:
                res.append(str(b))
                num = a
        return sign + "".join(res[::-1])
        
