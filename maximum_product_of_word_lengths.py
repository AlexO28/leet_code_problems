# Given a string array words, return the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. If no such two words exist, return 0.


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        words_set = []
        for word in words:
            words_set.append(set(list(word)))
        max_product = 0
        for i in range(len(words_set)-1):
            for j in range(i+1, len(words_set)):
                if len(words_set[i].intersection(words_set[j])) == 0:
                    max_product = max(max_product, len(words[i]) * len(words[j]))
        return max_product
