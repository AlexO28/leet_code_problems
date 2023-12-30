# You are given an array of strings words (0-indexed).
# In one operation, pick two distinct indices i and j, where words[i] is a non-empty string, and move any character from words[i] to any position in words[j].
# Return true if you can make every string in words equal using any number of operations, and false otherwise.
class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        freq_dict = {}
        for word in words:
            letters = list(word)
            for letter in letters:
                if letter in freq_dict:
                    freq_dict[letter] += 1
                else:
                    freq_dict[letter] = 1
        for elem in freq_dict.keys():
            if freq_dict[elem] % len(words) != 0:
                return False
        return True 
 
