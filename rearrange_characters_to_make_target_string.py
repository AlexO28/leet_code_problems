# You are given two 0-indexed strings s and target. You can take some letters from s and rearrange them to form new strings.
# Return the maximum number of copies of target that can be formed by taking letters from s and rearranging them.
class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        target_freq = {}
        for letter in list(target):
            if letter in target_freq:
                target_freq[letter] += 1
            else:
                target_freq[letter] = 1
        text_dict = {}
        for letter in list(s):
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
