# You are given a string s. An awesome substring is a non-empty substring of s such that we can make any number of swaps in order to make it a palindrome.
# Return the length of the maximum length awesome substring of s.
class Solution:
    def longestAwesome(self, s: str) -> int:
        parity_mask = 0
        first_occurrence = {0: -1}
        max_length = 1
        for current_index, char in enumerate(s):
            digit = int(char)
            parity_mask ^= 1 << digit
            if parity_mask in first_occurrence:
                max_length = max(
                    max_length, current_index - first_occurrence[parity_mask]
                )
            else:
                first_occurrence[parity_mask] = current_index
            for digit_to_flip in range(10):
                target_mask = parity_mask ^ (1 << digit_to_flip)
                if target_mask in first_occurrence:
                    max_length = max(
                        max_length, current_index - first_occurrence[target_mask]
                    )
        return max_length
