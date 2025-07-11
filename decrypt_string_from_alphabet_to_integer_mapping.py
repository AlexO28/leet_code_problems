# You are given a string s formed by digits and '#'. We want to map s to English lowercase characters as follows:
# Characters ('a' to 'i') are represented by ('1' to '9') respectively.
# Characters ('j' to 'z') are represented by ('10#' to '26#') respectively.
# Return the string formed after mapping.
# The test cases are generated so that a unique mapping will always exist.
class Solution:
    def freqAlphabets(self, s: str) -> str:
        mapping = {
            "1": "a",
            "2": "b",
            "3": "c",
            "4": "d",
            "5": "e",
            "6": "f",
            "7": "g",
            "8": "h",
            "9": "i",
            "10#": "j",
            "11#": "k",
            "12#": "l",
            "13#": "m",
            "14#": "n",
            "15#": "o",
            "16#": "p",
            "17#": "q",
            "18#": "r",
            "19#": "s",
            "20#": "t",
            "21#": "u",
            "22#": "v",
            "23#": "w",
            "24#": "x",
            "25#": "y",
            "26#": "z",
        }
        res = []
        j = len(s) - 1
        while j >= 0:
            if s[j] == "#":
                res.append(mapping[s[(j - 2) : (j + 1)]])
                j -= 3
            else:
                res.append(mapping[s[j]])
                j -= 1
        return "".join(res[::-1])
