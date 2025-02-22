# You are given two strings stamp and target. Initially, there is a string s of length target.length with all s[i] == '?'.
# In one turn, you can place stamp over s and replace every letter in the s with the corresponding letter from stamp.
# For example, if stamp = "abc" and target = "abcba", then s is "?????" initially. In one turn you can:
# place stamp at index 0 of s to obtain "abc??",
# place stamp at index 1 of s to obtain "?abc?", or
# place stamp at index 2 of s to obtain "??abc".
# Note that stamp must be fully contained in the boundaries of s in order to stamp (i.e., you cannot place stamp at index 3 of s).
# We want to convert s to target using at most 10 * target.length turns.
# Return an array of the index of the left-most letter being stamped at each turn. If we cannot obtain target from s within 10 * target.length turns, return an empty array.
from collections import deque
from typing import List


class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        indegrees = [len(stamp)] * (len(target) - len(stamp) + 1)
        queue = deque()
        graph = [[] for i in range(len(target))]
        for i in range(len(target) - len(stamp) + 1):
            for j in range(len(stamp)):
                if target[i + j] == stamp[j]:
                    indegrees[i] -= 1
                    if indegrees[i] == 0:
                        queue.append(i)
                else:
                    graph[i + j].append(i)      
        result = []
        visited = [False] * len(target)
        while queue:
            position = queue.popleft()
            result.append(position)
            for j in range(len(stamp)):
                if not visited[position + j]:
                    visited[position + j] = True
                    for dependency in graph[position + j]:
                        indegrees[dependency] -= 1
                        if indegrees[dependency] == 0:
                            queue.append(dependency)
        if all(visited):
            return result[::-1]
        else:
            return []
