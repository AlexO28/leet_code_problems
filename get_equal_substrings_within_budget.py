# You are given two strings s and t of the same length and an integer maxCost.
# You want to change s to t. Changing the ith character of s to ith character of t costs |s[i] - t[i]| (i.e., the absolute difference between the ASCII values of the characters).
# Return the maximum length of a substring of s that can be changed to be the same as the corresponding substring of t with a cost less than or equal to maxCost. If there is no substring from s that can be changed to its corresponding substring from t, return 0.
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        total_cost = 0
        start = 0
        max_length = 0
        for end in range(len(s)):
            total_cost += abs(ord(s[end]) - ord(t[end]))
            while total_cost > maxCost:
                total_cost -= abs(ord(s[start]) - ord(t[start]))
                start += 1
            max_length = max(max_length, end - start + 1)
        return max_length
