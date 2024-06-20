# Given a string s and an array of strings words, return the number of words[i] that is a subsequence of s.
# A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        count = 0
        answer_dict = {}
        for word in words:
            if word in answer_dict:
                if answer_dict[word]:
                    count += 1
            else:
                if self.isSubsequence(s, word):
                    count += 1
                    answer_dict[word] = True
                else:
                    answer_dict[word] = False
        return count

    def isSubsequence(self, s, word):
        if len(word) > len(s):
            return False
        i = 0
        j = 0
        for i in range(len(s)):
            if s[i] == word[j]:
                j += 1
                if j == len(word):
                    return True
        return False
