# A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:
# Every adjacent pair of words differs by a single letter.
# Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
# sk == endWord
# Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.


class Solution:

    def dfs(self, path, cur, beginWord, prev, ans):
        if cur == beginWord:
            ans.append(path[::-1])
            return
        for precursor in prev[cur]:
            path.append(precursor)
            self.dfs(path, precursor, beginWord, prev, ans)
            path.pop()

    def findLadders(self, beginWord, endWord, wordList):
        ans = []
        words = set(wordList)
        if endWord not in words:
            return ans
        words.discard(beginWord)
        dist = {beginWord: 0}
        prev = defaultdict(set)
        q = deque([beginWord])
        found = False
        step = 0
        while q and not found:
            step += 1
            for _ in range(len(q), 0, -1):
                p = q.popleft()
                s = list(p)
                for i in range(len(s)):
                    ch = s[i]
                    for j in range(26):
                        s[i] = chr(ord('a') + j)
                        t = ''.join(s)
                        if dist.get(t, 0) == step:
                            prev[t].add(p)
                        if t not in words: 
                            continue
                        prev[t].add(p)
                        words.discard(t)
                        q.append(t)
                        dist[t] = step
                        if endWord == t:
                            found = True
                    s[i] = ch
        if found:
            path = [endWord]
            self.dfs(path, endWord, beginWord, prev, ans)
        return ans

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        ladders = self.findLadders(beginWord, endWord, wordList)
        if len(ladders) == 0:
            return 0
        return len(ladders[0])
