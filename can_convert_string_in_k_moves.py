# Given two strings s and t, your goal is to convert s into t in k moves or less.
# During the ith (1 <= i <= k) move you can:
# Choose any index j (1-indexed) from s, such that 1 <= j <= s.length and j has not been chosen in any previous move, and shift the character at that index i times.
# Do nothing.
# Shifting a character means replacing it by the next letter in the alphabet (wrapping around so that 'z' becomes 'a'). Shifting a character by i means applying the shift operations i times.
# Remember that any index j can be picked at most once.
# Return true if it's possible to convert s into t in no more than k moves, otherwise return false.
class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if s == t:
            return True
        if len(s) != len(t):
            return False
        s = list(s)
        t = list(t)
        shifts = {}
        for j in range(len(s)):
            if s[j] != t[j]:
                delta = ord(t[j]) - ord(s[j])
                if delta < 0:
                    delta += 26
                if delta in shifts:
                    shifts[delta] += 26
                else:
                    shifts[delta] = delta
        return k >= max(shifts[delta] for delta in shifts)
