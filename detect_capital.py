# We define the usage of capitals in a word to be right when one of the following cases holds:
# All letters in this word are capitals, like "USA".
# All letters in this word are not capitals, like "leetcode".
# Only the first letter in this word is capital, like "Google".
# Given a string word, return true if the usage of capitals in it is right.
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if self.isCapital(word[0]):
            if len(word) <= 2:
                return True
            check = self.isCapital(word[1])
            for j in range(2, len(word)):
                if self.isCapital(word[j]) != check:
                    return False
            return True
        else:
            if len(word) == 1:
                return True
            for j in range(1, len(word)):
                if self.isCapital(word[j]):
                    return False
            return True

    def isCapital(self, symb):
        return symb == symb.upper()
