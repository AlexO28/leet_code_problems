Given a string s consisting of words and spaces, return the length of the last word in the string.
A word is a maximal substring consisting of non-space characters only.

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split(' ')
        for j in range(len(words)):
            if len(words[len(words)-j-1]) > 0:
                return len(words[len(words)-j-1])
        return 0
