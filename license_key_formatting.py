# You are given a license key represented as a string s that consists of only alphanumeric characters and dashes. The string is separated into n + 1 groups by n dashes. You are also given an integer k.
# We want to reformat the string s such that each group contains exactly k characters, except for the first group, which could be shorter than k but still must contain at least one character. Furthermore, there must be a dash inserted between two groups, and you should convert all lowercase letters to uppercase.
# Return the reformatted license key.
class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.upper().split("-")
        if len(s) == 1:
            s_list = list(s[0])
        else:
            s_list = list(s[0])
            for j in range(1, len(s)):
                s_list.extend(list(s[j]))
        if len(s_list) <= k:
            return "".join(s_list)
        else:
            res = []
            num_iter, rel = divmod(len(s_list), k)
            for i in range(num_iter):
                res.append("".join(s_list[(len(s_list)-k*(i+1)):(len(s_list)-i*k)]))
            if rel > 0:
                res.append("".join(s_list[0:(rel)]))
            return "-".join(res[::-1])
