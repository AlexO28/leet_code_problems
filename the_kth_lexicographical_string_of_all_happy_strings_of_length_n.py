# A happy string is a string that:
# consists only of letters of the set ['a', 'b', 'c'].
# s[i] != s[i + 1] for all values of i from 1 to s.length - 1 (string is 1-indexed).
# For example, strings "abc", "ac", "b" and "abcbabcbcb" are all happy strings and strings "aa", "baa" and "ababbc" are not happy strings.
# Given two integers n and k, consider a list of all happy strings of length n sorted in lexicographical order.# 
# Return the kth string of this list or return an empty string if there are less than k happy strings of length n.
class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        res = self.generateHappyStrings(n)
        res.sort()
        if len(res) < k:
            return ""
        else:
            return res[k-1]

    def generateHappyStrings(self, n):
        if n == 1:
            return ["a", "b", "c"]
        else:
            res = self.generateHappyStrings(n-1)
            new_res = []
            for line in res:
                if line[-1] == "a":
                    new_res.append(line + "b")
                    new_res.append(line + "c")
                elif line[-1] == "b":
                    new_res.append(line + "a")
                    new_res.append(line + "c")
                else:
                    new_res.append(line + "a")
                    new_res.append(line + "b")
            new_res = list(set(new_res))
            return new_res
