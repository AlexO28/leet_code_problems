# You are given two 0-indexed arrays of strings startWords and targetWords. Each string consists of lowercase English letters only.
# For each string in targetWords, check if it is possible to choose a string from startWords and perform a conversion operation on it to be equal to that from targetWords.
# The conversion operation is described in the following two steps:
# Append any lowercase letter that is not present in the string to its end.
# Rearrange the letters of the new string in any arbitrary order.
# Return the number of strings in targetWords that can be obtained by performing the operations on any string of startWords.
# Note that you will only be verifying if the string in targetWords can be obtained from a string in startWords by performing the operations. The strings in startWords do not actually change during this process.
from typing import List


class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        s = {sum(1 << (ord(c) - ord('a')) for c in w) for w in startWords}
        ans = 0
        for w in targetWords:
            x = sum(1 << (ord(c) - ord('a')) for c in w)
            for c in w:
                if x ^ (1 << (ord(c) - ord('a'))) in s:
                    ans += 1
                    break
        return ans
