# You are given a string s consisting only of uppercase English letters.
# You can apply some operations to this string where, in one operation, you can remove any occurrence of one of the substrings "AB" or "CD" from s.
# Return the minimum possible length of the resulting string that you can obtain.
# Note that the string concatenates after removing the substring and could produce new "AB" or "CD" substrings.
class Solution:
    def minLength(self, s: str) -> int:
        s = list(s)
        while True:
            if len(s) <= 1:
                return len(s)
            s_new = []
            ind = 0
            while ind < len(s):
                if s[ind] == "A":
                    if ind < len(s)-1:
                        if s[ind+1] == "B":
                            ind += 2
                        else:
                            s_new.append(s[ind])
                            ind += 1
                    else:
                        s_new.append(s[ind])
                        ind += 1
                elif s[ind] == "C":
                    if ind < len(s)-1:
                        if s[ind+1] == "D":
                            ind += 2
                        else:
                            s_new.append(s[ind])
                            ind += 1
                    else:
                        s_new.append(s[ind])
                        ind += 1
                else:
                    s_new.append(s[ind])
                    ind += 1
            if len(s_new) == len(s):
                return len(s)
            s = s_new.copy()
