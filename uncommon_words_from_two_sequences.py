# A sentence is a string of single-space separated words where each word consists only of lowercase letters.
# A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.
# Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        freq_dict_1 = {}
        for elem in s1.split(" "):
            if elem in freq_dict_1:
                freq_dict_1[elem] = 2
            else:
                freq_dict_1[elem] = 1
        freq_dict_2 = {}
        for elem in s2.split(" "):
            if elem in freq_dict_2:
                freq_dict_2[elem] = 2
            else:
                freq_dict_2[elem] = 1
        words_1 = [word for word in freq_dict_1 if (freq_dict_1[word] == 1) and (word not in freq_dict_2)]
        words_2 = [word for word in freq_dict_2 if (freq_dict_2[word] == 1) and (word not in freq_dict_1)]
        words_1.extend(words_2)
        return words_1
