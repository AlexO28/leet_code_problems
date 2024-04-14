# A message containing letters from A-Z can be encoded into numbers using the following mapping:
# 'A' -> "1"
# 'B' -> "2"
# ...
# 'Z' -> "26"
# To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:
# "AAJF" with the grouping (1 1 10 6)
# "KJF" with the grouping (11 10 6)
# Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".
# In addition to the mapping above, an encoded message may contain the '*' character, which can represent any digit from '1' to '9' ('0' is excluded). For example, the encoded message "1*" may represent any of the encoded messages "11", "12", "13", "14", "15", "16", "17", "18", or "19". Decoding "1*" is equivalent to decoding any of the encoded messages it can represent.
# Given a string s consisting of digits and '*' characters, return the number of ways to decode it.
# Since the answer may be very large, return it modulo 109 + 7. 
class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 0:
            return 0
        MOD = 10 ** 9 + 7
        prev_but_one = 0
        prev = 1
        current = 0
        for i in range(1, len(s)+1):
            if s[i-1] == "*":
                current = 9 * prev % MOD
            elif s[i-1] == "0":
                current = 0
            else:
                current = prev
            if i > 1:
                if (s[i-2] == "*") and (s[i-1] == "*"):
                    current = (current + 15 * prev_but_one) % MOD
                elif s[i-2] == "*":
                    if (s[i-1] == "7") or (s[i-1] == "8") or (s[i-1] == "9"):
                        current = (current + prev_but_one) % MOD
                    else:
                        current = (current + 2*prev_but_one) % MOD
                elif s[i-1] == "*":
                    if s[i-2] == "1":
                        current = (current + 9*prev_but_one) % MOD
                    elif s[i-2] == "2":
                        current = (current + 6*prev_but_one) % MOD
                elif (s[i-2] != "0"):
                    if int(s[(i-2):i]) <= 26:
                        current = (current + prev_but_one) % MOD
            prev_but_one, prev = prev, current
        return current    
        
