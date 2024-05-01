# Given a 0-indexed string word and a character ch, reverse the segment of word that starts at index 0 and ends at the index of the first occurrence of ch (inclusive). If the character ch does not exist in word, do nothing.
# For example, if word = "abcdefd" and ch = "d", then you should reverse the segment that starts at 0 and ends at 3 (inclusive). The resulting string will be "dcbaefd".
# Return the resulting string.
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if (len(word) == 1) or (word[0] == ch):
            return word
        j = 1
        found = False
        while j < len(word):
            if word[j] == ch:
                found = True
                break
            else:
                j += 1
        if found:
            if j == len(word) - 1:
                return word[::-1]
            else:
                return word[:(j+1)][::-1] + word[j+1:]
        else:
            return word
