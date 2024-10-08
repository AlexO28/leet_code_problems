# You are given a 0-indexed string s that you must perform k replacement operations on. The replacement operations are given as three 0-indexed parallel arrays, indices, sources, and targets, all of length k.
# To complete the ith replacement operation:
# Check if the substring sources[i] occurs at index indices[i] in the original string s.
# If it does not occur, do nothing.
# Otherwise if it does occur, replace that substring with targets[i].
# For example, if s = "abcd", indices[i] = 0, sources[i] = "ab", and targets[i] = "eee", then the result of this replacement will be "eeecd".
# All replacement operations must occur simultaneously, meaning the replacement operations should not affect the indexing of each other. The testcases will be generated such that the replacements will not overlap.
# For example, a testcase with s = "abc", indices = [0, 1], and sources = ["ab","bc"] will not be generated because the "ab" and "bc" replacements overlap.
# Return the resulting string after performing all replacement operations on s.
# A substring is a contiguous sequence of characters in a string.
class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        main_struct = {}
        for j in range(len(indices)):
            if indices[j] in main_struct:
                main_struct[indices[j]].append([sources[j], targets[j]])
            else:
                main_struct[indices[j]] = [[sources[j], targets[j]]]
        keys = list(main_struct.keys())
        keys.sort(reverse=True)
        res = s
        for key in keys:
            if key < len(s):
                for pair in main_struct[key]:
                    start_pos = key
                    end_pos = key + len(pair[0])
                    if end_pos <= len(s):
                        if s[start_pos:end_pos] == pair[0]:
                            if len(res) == 1:
                                res = pair[1]
                            elif end_pos >= len(res):
                                res = res[:start_pos] + pair[1]
                            elif start_pos == 0:
                                res = pair[1] + res[end_pos:]
                            else:
                                res = res[:start_pos] + pair[1] + res[end_pos:]
        return res
