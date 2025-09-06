# Given the string s, return the size of the longest substring containing each vowel an even number of times. That is, 'a', 'e', 'i', 'o', and 'u' must appear an even number of times.
class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        first_occurrence = {0: -1}
        max_length = 0
        current_mask = 0
        for index, char in enumerate(s):
            if char in "aeiou":
                bit_position = ord(char) - ord("a")
                current_mask ^= 1 << bit_position
            if current_mask in first_occurrence:
                previous_index = first_occurrence[current_mask]
                substring_length = index - previous_index
                max_length = max(max_length, substring_length)
            else:
                first_occurrence[current_mask] = index
        return max_length
