# Run-length encoding is a string compression method that works by replacing consecutive identical characters (repeated 2 or more times) with the concatenation of the character and the number marking the count of the characters (length of the run). For example, to compress the string "aabccc" we replace "aa" by "a2" and replace "ccc" by "c3". Thus the compressed string becomes "a2bc3".
# Notice that in this problem, we are not adding '1' after single characters.
# Given a string s and an integer k. You need to delete at most k characters from s such that the run-length encoded version of s has minimum length.
# Find the minimum length of the run-length encoded version of s after deleting at most k characters.
class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        self.s = s
        self.dp = [[101] * (k + 1) for _ in range(len(s))]
        return self.find_min_compression(0, k)

    def get_compression_length(self, frequency):
        if frequency == 1:
            return 1
        if frequency < 10:
            return 2
        if frequency < 100:
            return 3
        return 4

    def find_min_compression(self, start_idx, deletions_left):
        if deletions_left < 0:
            return 101
        if start_idx == len(self.s) or len(self.s) - start_idx <= deletions_left:
            return 0
        if self.dp[start_idx][deletions_left] != 101:
            return self.dp[start_idx][deletions_left]
        char_count = {}
        max_frequency = 0
        for end_idx in range(start_idx, len(self.s)):
            current_char = self.s[end_idx]
            char_count[current_char] = char_count.get(current_char, 0) + 1
            max_frequency = max(max_frequency, char_count[current_char])
            window_size = end_idx - start_idx + 1
            deletions_needed = window_size - max_frequency
            compression_length = self.get_compression_length(max_frequency)
            total_length = compression_length + self.find_min_compression(
                end_idx + 1, deletions_left - deletions_needed
            )
            self.dp[start_idx][deletions_left] = min(
                self.dp[start_idx][deletions_left], total_length
            )
        return self.dp[start_idx][deletions_left]
