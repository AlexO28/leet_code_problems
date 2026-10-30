# You are given an array words of size n consisting of non-empty strings.
# We define the score of a string term as the number of strings words[i] such that term is a prefix of words[i].
# For example, if words = ["a", "ab", "abc", "cab"], then the score of "ab" is 2, since "ab" is a prefix of both "ab" and "abc".
# Return an array answer of size n where answer[i] is the sum of scores of every non-empty prefix of words[i].
# Note that a string is considered as a prefix of itself.
class Solution:
    def sumPrefixScores(self, words: list[str]) -> list[int]:
        trie = Trie()
        for w in words:
            trie.insert(w)
        return [trie.search(w) for w in words]


class Trie:
    def __init__(self):
        self.children = [None] * 26
        self.cnt = 0
        self.acode = ord("a")

    def insert(self, w):
        node = self
        for c in w:
            idx = ord(c) - self.acode
            if node.children[idx] is None:
                node.children[idx] = Trie()
            node = node.children[idx]
            node.cnt += 1

    def search(self, w):
        node = self
        res = 0
        for c in w:
            idx = ord(c) - self.acode
            if node.children[idx] is None:
                return res
            else:
                node = node.children[idx]
                res += node.cnt
        return res
