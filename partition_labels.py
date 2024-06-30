# You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.
# Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.
# Return a list of integers representing the size of these parts.
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        if len(s) == 1:
            return [1]
        symb_dict = {}
        for i in range(len(s)):
            symb_dict[s[i]] = i
        pieces = []
        start = 0
        current = 0
        end = 0
        while start < len(s):
            end = max(end, symb_dict[s[current]])
            current += 1
            if current > end:
                pieces.append(end-start+1)
                start = current
                end = current
        return pieces
