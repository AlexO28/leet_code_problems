# A sentence is a list of tokens separated by a single space with no leading or trailing spaces. Every token is either a positive number consisting of digits 0-9 with no leading zeros, or a word consisting of lowercase English letters.
# Given a string s representing a sentence, you need to check if all the numbers in s are strictly increasing from left to right (i.e., other than the last number, each number is strictly smaller than the number on its right in s).
# Return true if so, or false otherwise.
class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        prev_num = -1
        s = s.split(" ")
        for elem in s:
            try:
                num = int(elem)
            except:
                continue
            if num > prev_num:
                prev_num = num
            else:
                return False
        return True
