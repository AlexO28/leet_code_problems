# Given a string s, return the number of segments in the string.
# A segment is defined to be a contiguous sequence of non-space characters.
class Solution:
    def countSegments(self, s: str) -> int:
        return len([segment for segment in s.split(" ") if len(segment) > 0])
