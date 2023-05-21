# Given a string s, return true if s is a valid number.


class Solution:
    def isNumber(self, s: str) -> bool:
        if s.lower() in ("inf", "+inf", "-inf", "infinity", "-infinity", "+infinity"):
            return False
        try:
            num = float(s)
            return True
        except:
            return False
