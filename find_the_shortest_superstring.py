# Given an array of strings words, return the smallest string that contains each string in words as a substring. If there are multiple valid strings of the smallest length, return any of them.
# You may assume that no string in words is a substring of another string in words.
from typing import List


class Solution:
    def shortestSuperstring(self, words: List[str]) -> str:
        overlap = [[0] * len(words) for i in range(len(words))]      
        for i in range(len(words)):
            for j in range(len(words)):
                if i != j:
                    for k in range(min(len(words[i]), len(words[j])), 0, -1):
                        if words[i][-k:] == words[j][:k]:
                            overlap[i][j] = k
                            break
        double_len = 1 << len(words)
        dp = [[0] * len(words) for i in range(double_len)]      
        parent = [[-1] * len(words) for i in range(double_len)]
        for mask in range(double_len):
            for j in range(len(words)):
                if (mask >> j) & 1:
                    prev_mask = mask ^ (1 << j)
                    for k in range(len(words)):
                        if (prev_mask >> k) & 1:
                            value = dp[prev_mask][k] + overlap[k][j]
                            if value > dp[mask][j]:
                                dp[mask][j] = value
                                parent[mask][j] = k
        last = max(range(len(words)), key=lambda i: dp[-1][i])
        order = []
        mask = double_len - 1
        while last != -1:
            prev = parent[mask][last]
            order.append(last)
            mask ^= (1 << last)
            last = prev
        order.reverse()
        order.extend(j for j in range(len(words)) if j not in order)
        result = [words[order[0]]]
        for i in range(1, len(order)):
            index = order[i]
            prev_index = order[i - 1]
            result.append(words[index][overlap[prev_index][index]:])      
        return "".join(result)
