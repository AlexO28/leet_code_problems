# In a string composed of 'L', 'R', and 'X' characters, like "RXXLRXRXL", a move consists of either replacing one occurrence of "XL" with "LX", or replacing one occurrence of "RX" with "XR". Given the starting string start and the ending string end, return True if and only if there exists a sequence of moves to transform one string to the other.
class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        if start == end:
            return True
        if len(start) == 1:
            return False
        startIndex = 0
        endIndex = 0
        while (startIndex < len(start)) or (endIndex < len(start)):
            while (startIndex < len(start)) and (start[startIndex] == "X"):
                startIndex += 1
            while (endIndex < len(start)) and (end[endIndex] == "X"):
                endIndex += 1
            if (startIndex == len(start)) and (endIndex == len(end)):
                return True
            elif (startIndex == len(start)):
                return False
            elif (endIndex == len(end)):
                return False
            if start[startIndex] != end[endIndex]:
                return False
            if (start[startIndex] == "R") and (startIndex > endIndex):
                return False
            if (start[startIndex] == "L") and (startIndex < endIndex):
                return False
            startIndex += 1
            endIndex += 1
        return True
