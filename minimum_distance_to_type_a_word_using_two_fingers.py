# You have a keyboard layout as shown above in the X-Y plane, where each English uppercase letter is located at some coordinate.
# For example, the letter 'A' is located at coordinate (0, 0), the letter 'B' is located at coordinate (0, 1), the letter 'P' is located at coordinate (2, 3) and the letter 'Z' is located at coordinate (4, 1).
# Given the string word, return the minimum total distance to type such string using only two fingers.
# The distance between coordinates (x1, y1) and (x2, y2) is |x1 - x2| + |y1 - y2|.
# Note that the initial positions of your two fingers are considered free so do not count towards your total distance, also your two fingers do not have to start at the first letter or the first two letters.
from math import inf


class Solution:
    def minimumDistance(self, word: str) -> int:
        dp = [[[inf] * 26 for i in range(26)] for j in range(len(word))]
        for j in range(26):
            dp[0][ord(word[0]) - ord("A")][j] = 0
            dp[0][j][ord(word[0]) - ord("A")] = 0
        for i in range(1, len(word)):
            prev_key = ord(word[i - 1]) - ord("A")
            current_key = ord(word[i]) - ord("A")
            travel_distance = self.calculate_distance(prev_key, current_key)
            for j in range(26):
                dp[i][current_key][j] = min(
                    dp[i][current_key][j], dp[i - 1][prev_key][j] + travel_distance
                )
                dp[i][j][current_key] = min(
                    dp[i][j][current_key], dp[i - 1][j][prev_key] + travel_distance
                )
                if j == prev_key:
                    for k in range(26):
                        switching_distance = self.calculate_distance(k, current_key)
                        dp[i][current_key][j] = min(
                            dp[i][current_key][j],
                            dp[i - 1][k][prev_key] + switching_distance,
                        )
                        dp[i][j][current_key] = min(
                            dp[i][j][current_key],
                            dp[i - 1][prev_key][k] + switching_distance,
                        )
        final_key_positions = dp[len(word) - 1][ord(word[-1]) - ord("A")]
        min_distance_with_final_key = min(final_key_positions)
        min_distance_with_final_key_other = min(
            dp[len(word) - 1][j][ord(word[-1]) - ord("A")] for j in range(26)
        )
        return int(min(min_distance_with_final_key, min_distance_with_final_key_other))

    def calculate_distance(self, key1, key2):
        row1, col1 = divmod(key1, 6)
        row2, col2 = divmod(key2, 6)
        return abs(row1 - row2) + abs(col1 - col2)
