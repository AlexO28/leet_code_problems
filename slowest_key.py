# A newly designed keypad was tested, where a tester pressed a sequence of n keys, one at a time.
# You are given a string keysPressed of length n, where keysPressed[i] was the ith key pressed in the testing sequence, and a sorted list releaseTimes, where releaseTimes[i] was the time the ith key was released. Both arrays are 0-indexed. The 0th key was pressed at the time 0, and every subsequent key was pressed at the exact time the previous key was released.
# The tester wants to know the key of the keypress that had the longest duration. The ith keypress had a duration of releaseTimes[i] - releaseTimes[i - 1], and the 0th keypress had a duration of releaseTimes[0].
# Note that the same key could have been pressed multiple times during the test, and these multiple presses of the same key may not have had the same duration.
# Return the key of the keypress that had the longest duration. If there are multiple such keypresses, return the lexicographically largest key of the keypresses.
from typing import List


class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        keys_info = {}
        keysPressed = list(keysPressed)
        for j in range(len(releaseTimes)):
            if j == 0:
                keys_info[keysPressed[j]] = releaseTimes[j]
            else:
                delta = releaseTimes[j] - releaseTimes[j - 1]
                if keysPressed[j] in keys_info:
                    keys_info[keysPressed[j]] = max(keys_info[keysPressed[j]], delta)
                else:
                    keys_info[keysPressed[j]] = delta
        max_time = max(list(keys_info.values()))
        res = []
        for key in keys_info:
            if keys_info[key] == max_time:
                res.append(key)
        res.sort()
        return res[-1]
