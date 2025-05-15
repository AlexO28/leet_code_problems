# Given a string s, return the last substring of s in lexicographical order.
class Solution:
    def lastSubstring(self, s: str) -> str:
        current_start = 0
        compare_start = 1
        offset = 0
        compare_start_offset = compare_start + offset
        current_start_offset = current_start + offset
        while compare_start_offset < len(s):
            if s[current_start_offset] == s[compare_start_offset]:
                offset += 1
                current_start_offset += 1
                compare_start_offset += 1
            elif s[current_start_offset] < s[compare_start_offset]:
                current_start = max(current_start + offset + 1, compare_start)
                offset = 0
                if current_start >= compare_start:
                    compare_start = current_start + 1
                compare_start_offset = compare_start
                current_start_offset = current_start
            else:
                compare_start += offset + 1
                offset = 0
                compare_start_offset = compare_start
                current_start_offset = current_start
        return s[current_start:]
