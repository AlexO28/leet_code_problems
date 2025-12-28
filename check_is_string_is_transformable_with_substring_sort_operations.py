# Given two strings s and t, transform string s into string t using the following operation any number of times:
# Choose a non-empty substring in s and sort it in place so the characters are in ascending order.
# For example, applying the operation on the underlined substring in "14234" results in "12344".
# Return true if it is possible to transform s into t. Otherwise, return false.
# A substring is a contiguous sequence of characters within a string.
from collections import defaultdict, deque


class Solution:
    def isTransformable(self, s: str, t: str) -> bool:
        pos = defaultdict(deque)
        for i, c in enumerate(s):
            pos[int(c)].append(i)
        for c in t:
            x = int(c)
            if not pos[x] or any(pos[i] and pos[i][0] < pos[x][0] for i in range(x)):
                return False
            pos[x].popleft()
        return True
