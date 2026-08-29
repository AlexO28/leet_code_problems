# You are given a string s and an integer repeatLimit. Construct a new string repeatLimitedString using the characters of s such that no letter appears more than repeatLimit times in a row. You do not have to use all characters from s.
# Return the lexicographically largest repeatLimitedString possible.
# A string a is lexicographically larger than a string b if in the first position where a and b differ, string a has a letter that appears later in the alphabet than the corresponding letter in b. If the first min(a.length, b.length) characters do not differ, then the longer string is the lexicographically larger one.
from collections import Counter


class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        freq_dict = Counter(s)
        res = []
        while True:
            keys = list(freq_dict.keys())
            if len(keys) == 0:
                break
            keys.sort(reverse = True)
            if len(res) > 0:
                if (len(keys) == 1) and (keys[0] == res[-1]):
                    break
            if freq_dict[keys[0]] > repeatLimit:
                res.extend([keys[0]] * repeatLimit)
                freq_dict[keys[0]] -= repeatLimit
                if len(keys) > 1:
                    res.append(keys[1])
                    freq_dict[keys[1]] -= 1
                    if freq_dict[keys[1]] == 0:
                        del freq_dict[keys[1]]
            else:
                res.extend([keys[0]] * freq_dict[keys[0]])
                del freq_dict[keys[0]]
        return "".join(res)
