# Given an array of strings words representing an English Dictionary, return the longest word in words that can be built one character at a time by other words in words.
# If there is more than one possible answer, return the longest word with the smallest lexicographical order. If there is no answer, return the empty string.
# Note that the word should be built from left to right with each additional character being added to the end of a previous word. 
from functools import cache


class Solution:
    def longestWord(self, words: List[str]) -> str:
        words = list(set(words))
        self.word_struct = {}
        for word in words:
            if len(word) in self.word_struct:
                self.word_struct[len(word)].append(word)
            else:
                self.word_struct[len(word)] = [word]
        prefix_results = self.find()
        max_level = max([len(prefix) for prefix in prefix_results])
        prefix_results = [prefix_result for prefix_result in prefix_results if len(prefix_result) == max_level]
        prefix_results.sort()
        return prefix_results[0]

    def find(self):
        if 1 in self.word_struct:
            prefix_results = []
            for prefix in self.word_struct[1]:
                prefix_res = self.findByPrefix(prefix)
                if len(prefix_res) > 0:
                    prefix_results.extend(prefix_res)
            if len(prefix_results) == 0:
                return [""]
            else:
                return prefix_results
        else:
            return [""]

    @cache
    def findByPrefix(self, prefix):
        next_level = len(prefix) + 1
        if next_level in self.word_struct:
            prefix_results = []
            for new_prefix in self.word_struct[next_level]:
                if new_prefix[:len(prefix)] == prefix:
                    prefix_addition = self.findByPrefix(new_prefix)
                    if len(prefix_addition) > 0:
                        prefix_results.extend(prefix_addition)
            if len(prefix_results) == 0:
                return [prefix]
            else:    
                return list(set(prefix_results))
        else:
            return [prefix]
