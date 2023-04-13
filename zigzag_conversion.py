# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
# And then read line by line: "PAHNAPLSIIGYIR"
# Write the code that will take a string and make this conversion given a number of rows


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        lines = ['']*numRows
        upWard = True
        start_line = 0
        for char in s:
            if upWard:
                lines[start_line] += char
                start_line += 1
                if start_line == numRows:
                    start_line = numRows - 1
                    upWard = False
            else:
                start_line -= 1
                lines[start_line] += char
                if start_line == 0:
                    upWard = True
                    start_line += 1
        return ''.join(lines)
