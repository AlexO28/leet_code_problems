# Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        number = columnNumber
        resstr = ""
        while number > 0:
            number, remainder = divmod(number-1, 26)
            resstr += alphabet[remainder]
        return resstr[::-1]
