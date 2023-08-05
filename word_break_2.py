# Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in any order.
# Note that the same word in the dictionary may be reused multiple times in the segmentation.


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        present_indices = []
        ways = {}
        if s[0] in wordDict:
            present_indices.append(0)
            ways[0] = [s[0]]
        if len(s) == 1:
            if (len(present_indices) > 0):
                return ways[0]
            else:
                return []
        for j in range(1, len(s)):
            substr = s[0:(j+1)]
            if substr in wordDict:
                present_indices.append(j)
                if j not in ways.keys():
                    ways[j] = [substr]
                else:
                    if substr not in ways[j]:
                        ways[j].append(substr)
            if len(present_indices) > 0:
                for present_index in present_indices:
                    substr = s[(present_index+1):(j+1)]
                    if substr in wordDict:
                        present_indices.append(j)
                        temp_list = (ways[present_index]).copy()
                        for i in range(len(temp_list)):
                            temp_list[i] += ' ' + substr
                        if j not in ways.keys():
                            ways[j] = temp_list
                        else:
                            ways[j].extend(temp_list)
                            ways[j] = list(set(ways[j]))
        if len(s) - 1 in present_indices:
            return ways[len(s) - 1]
        else:
            return []
