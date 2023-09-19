# Given a pattern and a string s, find if s follows the same pattern.


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(' ')
        if len(words) != len(pattern):
            return False
        short_words = list(dict.fromkeys(words))
        word_dict = {}
        letters = list(dict.fromkeys(list(pattern)))
        if len(letters) != len(short_words):
            return False
        for j in range(len(letters)):
            word_dict[letters[j]] = short_words[j]
        word_list = []
        for letter in pattern:
            word_list.append(word_dict[letter])
        return word_list == words
        
