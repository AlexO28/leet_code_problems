# Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.
# Return any possible rearrangement of s or return "" if not possible.
class Solution:
    def reorganizeString(self, s: str) -> str:
        if len(s) == 1:
            return s
        freq_dict = {}
        for elem in s:
            if elem in freq_dict:
                freq_dict[elem] += 1
            else:
                freq_dict[elem] = 1
        if max(list(freq_dict.values())) > (len(s) + 1) // 2:
            return ""
        s_new = []
        keys = [elem[0] for elem in sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)]
        ind = 0
        s_new = [None]*len(s)
        keys_ind = 0
        num_iter = 0
        while num_iter < len(s_new):
            if freq_dict[keys[keys_ind]] == 0:
                keys_ind += 1
            freq_dict[keys[keys_ind]] -= 1
            s_new[ind] = keys[keys_ind]
            ind += 2
            if ind >= len(s_new):
                ind = 1
            num_iter += 1
        return "".join(s_new)
