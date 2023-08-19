# Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number.

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        num = 0
        degree = 1
        for j in range(len(columnTitle)):
            ind = alphabet.index(columnTitle[len(columnTitle)-j-1]) + 1
            num += ind * degree
            degree *= 26
        return num
