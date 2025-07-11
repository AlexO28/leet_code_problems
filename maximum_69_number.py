# You are given a positive integer num consisting only of digits 6 and 9.
# Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).
class Solution:
    def maximum69Number(self, num: int) -> int:
        num_str = str(num)
        if "6" in num_str:
            res = []
            found = False
            for digit in list(num_str):
                if digit == "9":
                    res.append(digit)
                else:
                    if not found:
                        found = True
                        res.append("9")
                    else:
                        res.append(digit)
            return int("".join(res))
        else:
            return num
