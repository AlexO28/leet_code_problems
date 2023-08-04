# Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.
# Note that the same word in the dictionary may be reused multiple times in the segmentation.

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        present_indices = []
        if s[0] in wordDict:
            present_indices.append(0)
        if len(s) == 1:
            return len(present_indices) > 0
        for j in range(1, len(s)):
            substr = s[0:(j+1)]
            if substr in wordDict:
                present_indices.append(j)
            else:
                if len(present_indices) > 0:
                    for present_index in present_indices:
                        substr = s[(present_index+1):(j+1)]
                        if substr in wordDict:
                            present_indices.append(j)
                            break
        return (len(s)-1) in present_indices
