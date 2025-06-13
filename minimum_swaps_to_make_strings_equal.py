# You are given two strings s1 and s2 of equal length consisting of letters "x" and "y" only. Your task is to make these two strings equal to each other. You can swap any two characters that belong to different strings, which means: swap s1[i] and s2[j].
# Return the minimum number of swaps required to make s1 and s2 equal, or return -1 if it is impossible to do so.
class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        count_xy = 0
        count_yx = 0
        for char1, char2 in zip(s1, s2):
            if (char1 == "x") and (char2 == "y"):
                count_xy += 1
            elif (char1 == "y") and (char2 == "x"):
                count_yx += 1
        if (count_xy + count_yx) % 2 > 0:
            return -1
        else:
            return (count_xy // 2) + (count_yx // 2) + 2 * (count_xy % 2)
