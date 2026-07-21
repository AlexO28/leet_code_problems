# You are given a binary string s of length n, where:
# '1' represents an active section.
# '0' represents an inactive section.
# You can perform at most one trade to maximize the number of active sections in s. In a trade, you:
# Convert a contiguous block of '1's that is surrounded by '0's to all '0's.
# Afterward, convert a contiguous block of '0's that is surrounded by '1's to all '1's.
# Return the maximum number of active sections in s after making the optimal trade.
# Note: Treat s as if it is augmented with a '1' at both ends, forming t = '1' + s + '1'. The augmented '1's do not contribute to the final count.
class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        num_ones = 0
        coding = []
        symb_type = "1"
        num_symbols = 0
        num_ones = 0
        for elem in s:
            if elem == "1":
                num_ones += 1
            if elem == symb_type:
                num_symbols += 1
            else:
                if num_symbols > 0:
                    coding.append([num_symbols, symb_type])
                symb_type = elem
                num_symbols = 1
        coding.append([num_symbols, symb_type])
        max_delta = 0
        if len(coding) > 2:
            for j in range(1, len(coding) - 1):
                if (
                    (coding[j][1] == "1")
                    and (coding[j - 1][1] == "0")
                    and (coding[j + 1][1] == "0")
                ):
                    max_delta = max(max_delta, coding[j - 1][0] + coding[j + 1][0])
        return num_ones + max_delta
