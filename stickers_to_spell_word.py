# We are given n different types of stickers. Each sticker has a lowercase English word on it.
# You would like to spell out the given string target by cutting individual letters from your collection of stickers and rearranging them. You can use each sticker more than once if you want, and you have infinite quantities of each sticker.
# Return the minimum number of stickers that you need to spell out target. If the task is impossible, return -1.
from collections import deque, Counter


class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        queue = deque([0])
        steps = 0
        visited = [False] * (1 << len(target))
        visited[0] = True  
        while queue:
            for j in range(len(queue)):
                current_state = queue.popleft()
                if current_state == (1 << len(target)) - 1:
                    return steps
                for sticker in stickers:
                    next_state = current_state
                    sticker_count = Counter(sticker)
                    for i, char in enumerate(target):
                        if not (next_state & (1 << i)) and sticker_count[char]:
                            next_state |= 1 << i
                            sticker_count[char] -= 1
                    if not visited[next_state]:
                        visited[next_state] = True
                        queue.append(next_state)
            steps += 1
        return -1
