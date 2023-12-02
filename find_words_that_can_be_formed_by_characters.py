# You are given an array of strings words and a string chars.
# A string is good if it can be formed by characters from chars (each character can only be used once).
# Return the sum of lengths of all good strings in words.


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars_freq = {}
        for s in chars:
            if s in chars_freq:
                chars_freq[s] += 1
            else:
                chars_freq[s] = 1
        res = 0
        for word in words:
            if len(word) <= len(chars):
                word_freq = {}
                terminate = False
                for s in word:
                    if s not in chars_freq:
                        terminate = True
                        break
                    if s in word_freq:
                        word_freq[s] += 1
                    else:
                        word_freq[s] = 1
                if not terminate:
                    for s in word_freq.keys():
                        if word_freq[s] > chars_freq[s]:
                            terminate = True
                            break
                    if not terminate:
                        res += len(word)
        return res
