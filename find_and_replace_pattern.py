# Given a list of strings words and a string pattern, return a list of words[i] that match pattern. You may return the answer in any order.
# A word matches the pattern if there exists a permutation of letters p so that after replacing every letter x in the pattern with p(x), we get the desired word.
# Recall that a permutation of letters is a bijection from letters to letters: every letter maps to another letter, and no two letters map to the same letter.
class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        res = []
        for word in words:
            word_dict = {}
            found = True
            for i in range(len(pattern)):
                if pattern[i] in word_dict:
                    if word[i] != word_dict[pattern[i]]:
                        found = False
                        break
                else:
                    word_dict[pattern[i]] = word[i]
            if found:
                if (len(word_dict)) == (len(set(word_dict.values()))):
                    res.append(word)
        return res
