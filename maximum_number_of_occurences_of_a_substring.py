# Given a string s, return the maximum number of occurrences of any substring under the following rules:
# The number of unique characters in the substring must be less than or equal to maxLetters.
# The substring size must be between minSize and maxSize inclusive.
class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        freq_dict = {}
        for i in range(len(s)):
            for j in range(i, len(s)):
                substr = s[i : (j + 1)]
                if len(substr) < minSize:
                    continue
                if len(substr) > maxSize:
                    break
                if len(set(list(substr))) <= maxLetters:
                    if substr in freq_dict:
                        freq_dict[substr] += 1
                    else:
                        freq_dict[substr] = 1
                else:
                    break
        if len(freq_dict) == 0:
            return 0
        else:
            return max(list(freq_dict.values()))
