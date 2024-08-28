# A valid encoding of an array of words is any reference string s and array of indices indices such that:
# words.length == indices.length
# The reference string s ends with the '#' character.
# For each index indices[i], the substring of s starting from indices[i] and up to (but not including) the next '#' character is equal to words[i].
# Given an array of words, return the length of the shortest reference string s possible of any valid encoding of words.
class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        root = TrieNode()
        for word in words:
            current_node = root
            for char in reversed(word):
                index = ord(char) - ord('a')
                if current_node.children[index] is None:
                    current_node.children[index] = TrieNode()
                current_node = current_node.children[index]
        return self.dfs(root, 1)

    def dfs(self, current_node, length):
        is_leaf = True
        encoding_length = 0
        for i in range(26):
            if current_node.children[i] is not None:
                is_leaf = False
                encoding_length += self.dfs(current_node.children[i], length + 1)              
        if is_leaf:
            encoding_length += length          
        return encoding_length
        
class TrieNode:
    def __init__(self):
        self.children = [None] * 26
