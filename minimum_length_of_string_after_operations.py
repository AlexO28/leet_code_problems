# You are given a string s.
# You can perform the following process on s any number of times:
# Choose an index i in the string such that there is at least one character to the left of index i that is equal to s[i], and at least one character to the right that is also equal to s[i].
# Delete the closest character to the left of index i that is equal to s[i].
# Delete the closest character to the right of index i that is equal to s[i].
# Return the minimum length of the final string s that you can achieve.
class Solution:
    def minimumLength(self, s: str) -> int:
        freq_dict = {}
        for elem in s:
            if elem in freq_dict:
                freq_dict[elem] += 1
            else:
                freq_dict[elem] = 1
        summa = 0
        for key in freq_dict:
            if freq_dict[key] > 2:
                if freq_dict[key] % 2 == 0:
                    summa += 2
                else:
                    summa += 1
            else:
                summa += freq_dict[key]
        return summa
