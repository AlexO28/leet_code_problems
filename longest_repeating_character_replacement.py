# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.
# Return the length of the longest substring containing the same letter you can get after performing the above operations.
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        frequency_counter = {}
        for elem in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            frequency_counter[elem] = 0
        left = 0
        right = 0
        max_frequency = 0
        while right < len(s):
            frequency_counter[s[right]] += 1
            max_frequency = max(max_frequency, frequency_counter[s[right]])
            if (right - left + 1) > max_frequency + k:
                frequency_counter[s[left]] -= 1
                left += 1          
            right += 1
        return right - left
  
