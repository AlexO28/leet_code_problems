# You are given a 0-indexed string s of even length n. The string consists of exactly n / 2 opening brackets '[' and n / 2 closing brackets ']'.
# A string is called balanced if and only if:
# It is the empty string, or
# It can be written as AB, where both A and B are balanced strings, or
# It can be written as [C], where C is a balanced string.
# You may swap the brackets at any two indices any number of times.
# Return the minimum number of swaps to make s balanced.
class Solution:
    def minSwaps(self, s: str) -> int:
        s = list(s)
        number_open = 0
        number_closed = 0
        start = 0
        end = len(s)-1
        number_of_swaps = 0
        while start < len(s):
            if s[start] == "[":
                number_open += 1
            else:
                number_closed += 1
            if number_closed > number_open:
                while s[end] == "]":
                    end -= 1
                s[start], s[end] = s[end], s[start]
                number_of_swaps += 1
                number_closed -= 1
                number_open += 1
            start += 1
        return number_of_swaps
