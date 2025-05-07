# Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.
# You can use each character in text at most once. Return the maximum number of instances that can be formed.
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        target_freq = {"b": 1, "a": 1, "l": 2, "o": 2, "n": 1}
        text_dict = {}
        for letter in list(text):
            if letter in target_freq:
                if letter in text_dict:
                    text_dict[letter] += 1
                else:
                    text_dict[letter] = 1
        min_val = None
        for letter in target_freq:
            if letter not in text_dict:
                return 0
            else:
                if min_val is None:
                    min_val = text_dict[letter] // target_freq[letter]
                else:
                    min_val = min(min_val, text_dict[letter] // target_freq[letter])
        return min_val
