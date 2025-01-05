# You are given a string s of lowercase English letters and a 2D integer array shifts where shifts[i] = [starti, endi, directioni]. For every i, shift the characters in s from the index starti to the index endi (inclusive) forward if directioni = 1, or shift the characters backward if directioni = 0.
# Shifting a character forward means replacing it with the next letter in the alphabet (wrapping around so that 'z' becomes 'a'). Similarly, shifting a character backward means replacing it with the previous letter in the alphabet (wrapping around so that 'a' becomes 'z').
# Return the final string after all such shifts to s are applied.
from typing import List


class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        a_code = ord("a")
        difference_array = [0] * (len(s) + 1)
        for shift in shifts:
            if shift[2] > 0:
                difference_array[shift[0]] += 1
                difference_array[shift[1] + 1] -= 1
            else:
                difference_array[shift[0]] -= 1
                difference_array[shift[1] + 1] += 1
        for i in range(1, len(s) + 1):
            difference_array[i] += difference_array[i - 1]
        return "".join(chr(a_code + ((ord(s[i]) - a_code + difference_array[i]) % 26)) for i in range(len(s)))
