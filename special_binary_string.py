class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        return self.processSpecialString(s)

    def processSpecialString(self, s):
        special_strings = []
        balance = 0
        start_index = 0
        for i in range(len(s)):
            if s[i] == "1":
                balance += 1
            else:
                balance -= 1
            if balance == 0:
                inner_special = "1" + self.processSpecialString(s[start_index + 1 : i]) + "0"
                special_strings.append(inner_special)
                start_index = i + 1
        special_strings.sort(reverse=True)
        return "".join(special_strings)
