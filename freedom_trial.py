# In the video game Fallout 4, the quest "Road to Freedom" requires players to reach a metal dial called the "Freedom Trail Ring" and use the dial to spell a specific keyword to open the door.
# Given a string ring that represents the code engraved on the outer ring and another string key that represents the keyword that needs to be spelled, return the minimum number of steps to spell all the characters in the keyword.
# Initially, the first character of the ring is aligned at the "12:00" direction. You should spell all the characters in key one by one by rotating ring clockwise or anticlockwise to make each character of the string key aligned at the "12:00" direction and then by pressing the center button.
# At the stage of rotating the ring to spell the key character key[i]:
# You can rotate the ring clockwise or anticlockwise by one place, which counts as one step. The final purpose of the rotation is to align one of ring's characters at the "12:00" direction, where this character must equal key[i].
# If the character key[i] has been aligned at the "12:00" direction, press the center button to spell, which also counts as one step. After the pressing, you could begin to spell the next character in the key (next stage). Otherwise, you have finished all the spelling.
from math import inf

class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        positions = {}
        for i in range(len(ring)):
            if ring[i] in positions:
                positions[ring[i]].append(i)
            else:
                positions[ring[i]] = [i]
        dp = [[inf] * len(ring) for i in range(len(key))]
        for j in positions[key[0]]:
            dp[0][j] = min(j, len(ring)-j) + 1
        for i in range(1, len(key)):
            for j in positions[key[i]]:
                for k in positions[key[i-1]]:
                    dp[i][j] = min(dp[i][j], dp[i-1][k] + min(abs(j-k), len(ring)-abs(j - k))+1)
        return min(dp[-1][j] for j in positions[key[-1]])
