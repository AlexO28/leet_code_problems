# Given a string s containing only lowercase English letters and the '?' character, convert all the '?' characters into lowercase letters such that the final string does not contain any consecutive repeating characters. You cannot modify the non '?' characters.
# It is guaranteed that there are no consecutive repeating characters in the given string except for '?'.
# Return the final string after all the conversions (possibly zero) have been made. If there is more than one solution, return any of them. It can be shown that an answer is always possible with the given constraints.
class Solution:
    def modifyString(self, s: str) -> str:
        new_s = []
        good = ["a", "b", "c"]
        for j in range(len(s)):
            if s[j] == "?":
                bad = []
                if j > 0:
                    bad.append(new_s[-1])
                if j < len(s) - 1:
                    if s[j + 1] != "?":
                        bad.append(s[j + 1])
                for elem in good:
                    if elem not in bad:
                        break
                new_s.append(elem)
            else:
                new_s.append(s[j])
        return "".join(new_s)
