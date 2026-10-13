# You are given a string num consisting of digits only.
# Return the largest palindromic integer (in the form of a string) that can be formed using digits taken from num. It should not contain leading zeroes.
# Notes:
# You do not need to use all the digits of num, but you must use at least one digit.
# The digits can be reordered.
class Solution:
    def largestPalindromic(self, num: str) -> str:
        num_dict = {}
        for i in range(len(num)):
            if num[i] in num_dict:
                num_dict[num[i]] += 1
            else:
                num_dict[num[i]] = 1
        line = []
        keys = list(num_dict.keys())
        keys.sort(reverse=True)
        for key in keys:
            while num_dict[key] > 1:
                if (key == "0") and (len(line) == 0):
                    break
                line.append(key)
                num_dict[key] -= 2
        extra = ""
        for key in keys:
            if num_dict[key] >= 1:
                extra = key
                break
        return "".join(line) + extra + "".join(line[::-1])
