# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        reference = strs[0]
        if len(strs) == 1:
            return reference
        not_found = False
        for i in range(len(reference)):
            for j in range(1, len(strs)):
                if i < len(strs[j]):
                    if strs[j][i] != reference[i]:
                        not_found = True
                        break
                else:
                    not_found = True
            if not_found:
                break
        if not not_found:
            return reference
        if i == 0:
            return ""
        return reference[0:i]
