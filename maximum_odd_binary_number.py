# You are given a binary string s that contains at least one '1'.
# You have to rearrange the bits in such a way that the resulting binary number is the maximum odd binary number that can be created from this combination.
class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        num_ones = len([elem for elem in s if elem == "1"])
        if num_ones == 1:
            if len(s) == 1:
                return s
            else:
                return "0"*(len(s)-1) + "1"
        else:
            if len(s) == num_ones:
                return s
            else:
                return "1"*(num_ones-1) + "0"*(len(s)-num_ones) + "1"
