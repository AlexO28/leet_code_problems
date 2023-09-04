# Given an m x n board of characters and a list of strings words, return all words on the board.
# Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

class Trie:
    def __init__(self):
        self.children = [None] * 26
        self.word = ''

    def insert(self, word):
        node = self
        for symb in word:
            idx = ord(symb) - ord('a')
            if node.children[idx] is None:
                node.children[idx] = Trie()
            node = node.children[idx]
        node.word = word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.insert(word)
        ans = set()
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                self.dfs(trie, i, j, board, ans, m, n)
        return list(ans)

    def dfs(self, node, i, j, board, ans, m, n):
        idx = ord(board[i][j]) - ord('a')
        if node.children[idx] is None:
            return
        node = node.children[idx]
        if node.word:
            ans.add(node.word)
        c = board[i][j]
        board[i][j] = '0'
        for a, b in [[0, -1], [0, 1], [1, 0], [-1, 0]]:
            x, y = i + a, j + b
            if 0 <= x < m and 0 <= y < n and board[x][y] != '0':
               self.dfs(node, x, y, board, ans, m, n)
        board[i][y] = c
