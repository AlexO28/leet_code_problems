# decode message consisting from symbols into letters
# we need to return the number of possible decodings for such message

class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 0:
            return 0
        dp = [0] * (len(s) + 1)
        dp[len(s)] = 1
        dp[len(s) - 1] = 0 if s[len(s) - 1] == '0' else 1
        for i in range(len(s) - 2, -1, -1):
            if s[i] == '0':
                continue
            temp = int(s[i:(i + 2)])
            if temp > 26:
                dp[i] = dp[i + 1]
            else:
                dp[i] = dp[i + 1] + dp[i + 2]
        return dp[0]
