# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_dict = {}
        for word in strs:
            letters = list(word)
            letters.sort()
            new_word = ''.join(letters)
            if new_word in word_dict.keys():
                word_dict[new_word].append(word)
            else:
                word_dict[new_word] = [word]
        res_list = []
        for word in word_dict.keys():
            res_list.append(word_dict[word])
        return res_list
