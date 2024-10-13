# You are given an encoded string s. To decode the string to a tape, the encoded string is read one character at a time and the following steps are taken:
# If the character read is a letter, that letter is written onto the tape.
# If the character read is a digit d, the entire current tape is repeatedly written d - 1 more times in total.
# Given an integer k, return the kth letter (1-indexed) in the decoded string.
class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        s = list(s)
        N = 0
        for i in range(len(s)):
            if s[i] in "0123456789":
                num = int(s[i])
                N *= num
            else:
                N += 1
            if N >= k:
                break
        while True:
            if s[i] in "0123456789":
                num = int(s[i])
                N /= num
                k %= N
            else:
                if k % N == 0:
                    return s[i]
                else:
                    N -= 1
            i -= 1
