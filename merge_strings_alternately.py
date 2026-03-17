# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.
# Return the merged string.
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        use_first = True
        ind1 = 0
        ind2 = 0
        res = []
        while (ind1 < len(word1)) or (ind2 < len(word2)):
            if use_first:
                res.append(word1[ind1])
                ind1 += 1
                if ind2 < len(word2):
                    use_first = False
            else:
                res.append(word2[ind2])
                ind2 += 1
                if ind1 < len(word1):
                    use_first = True
        return "".join(res)
