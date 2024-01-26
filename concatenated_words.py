# Given an array of strings words (without duplicates), return all the concatenated words in the given list of words.
# A concatenated word is defined as a string that is comprised entirely of at least two shorter words (not necessarily distinct) in the given array.
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        if len(words) == 1:
            return []
        res = []
        trie = Trie()
        words.sort(key=len)
        for word in words:
            if self.dfs(word, trie):
                res.append(word)
            else:
                trie.insert(word)
        return res

    def dfs(self, word, trie):
        if not word:
            return True
        node = trie
        for i, char in enumerate(word):
            index = ord(char) - ord('a')
            if node.children[index] is None:
                return False
            node = node.children[index]
            if node.is_end_of_word and self.dfs(word[i+1:], trie):
                return True
        return False


class Trie:
    def __init__(self):
        self.children = [None] * 26
        self.is_end_of_word = False

    def insert(self, word):
        node = self
        for char in word:
            index = ord(char) - ord('a')
            if node.children[index] is None:
                node.children[index] = Trie()
            node = node.children[index]
        node.is_end_of_word = True
