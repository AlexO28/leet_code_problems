# Given a string s of lower and upper case English letters.
# A good string is a string which doesn't have two adjacent characters s[i] and s[i + 1] where:
# 0 <= i <= s.length - 2
# s[i] is a lower-case letter and s[i + 1] is the same letter but in upper-case or vice-versa.
# To make the string good, you can choose two adjacent characters that make the string bad and remove them. You can keep doing this until the string becomes good.
# Return the string after making it good. The answer is guaranteed to be unique under the given constraints.
# Notice that an empty string is also good.
class Solution:
    def makeGood(self, s: str) -> str:
        s = list(s)
        while True:
            if len(s) <= 1:
                return ''.join(s)
            else:
                deleted = False
                for j in range(1, len(s)):
                    new_charact_2 = s[j].lower() 
                    new_charact_1 = s[j-1].lower()
                    if (new_charact_1 == new_charact_2) and (((new_charact_1 != s[j-1] and new_charact_2 == s[j]) or ((new_charact_1 == s[j-1] and new_charact_2 != s[j])))):
                        del s[j]
                        del s[j-1]
                        deleted = True
                        break
                if not deleted:
                    return ''.join(s)
