# Given 3 positives numbers a, b and c. Return the minimum flips required in some bits of a and b to make ( a OR b == c ). (bitwise OR operation).
# Flip operation consists of change any single bit 1 to 0 or change the bit 0 to 1 in their binary representation.
class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        a = bin(a)[2:]
        b = bin(b)[2:]
        c = bin(c)[2:]
        max_len = max(len(a), len(b), len(c))
        if len(a) < max_len:
            a = "0" * (max_len - len(a)) + a
        if len(b) < max_len:
            b = "0" * (max_len - len(b)) + b
        if len(c) < max_len:
            c = "0" * (max_len - len(c)) + c
        number_of_flips = 0
        for j in range(max_len):
            if c[j] == "1":
                if (a[j] == "0") and (b[j] == "0"):
                    number_of_flips += 1
            else:
                if a[j] == "1":
                    number_of_flips += 1
                if b[j] == "1":
                    number_of_flips += 1
        return number_of_flips
