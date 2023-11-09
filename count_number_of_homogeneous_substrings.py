# Given a string s, return the number of homogenous substrings of s. Since the answer may be too large, return it modulo 109 + 7.
# A string is homogenous if all the characters of the string are the same.


class Solution:
    def countHomogenous(self, s: str) -> int:
        prev_val = ""
        freq = 0
        num = 0
        max_val = 7 + 10 ** 9
        for symb in s:
            if symb == prev_val:
                freq += 1
            else:
                num += int((freq/2)*(freq + 1))
                if num >= max_val:
                    num = num % max_val
                prev_val = symb
                freq = 1
        num += int((freq/2)*(freq + 1))
        if num >= max_val:
            num = num % max_val
        return num
