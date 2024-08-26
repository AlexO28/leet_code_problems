# We had some 2-dimensional coordinates, like "(1, 3)" or "(2, 0.5)". Then, we removed all commas, decimal points, and spaces and ended up with the string s.
# Return a list of strings representing all possibilities for what our original coordinates could have been.
# Our original representation never had extraneous zeroes, so we never started with numbers like "00", "0.0", "0.00", "1.0", "001", "00.01", or any other number that can be represented with fewer digits. Also, a decimal point within a number never occurs without at least one digit occurring before it, so we never started with numbers like ".1".
# The final answer list can be returned in any order. All coordinates in the final answer have exactly one space between them (occurring after the comma.)
class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        s = s[1:(-1)]
        res = []
        for j in range(len(s)-1):
            left_numbers = self.extractNumbers(s[:(j+1)])
            right_numbers = self.extractNumbers(s[(j+1):])
            if (len(left_numbers) > 0) and (len(right_numbers) > 0):
                for number1 in left_numbers:
                    for number2 in right_numbers:
                        res.append("(" + str(number1) + ", " + str(number2) + ")")
        return res

    def extractNumbers(self, s):
        if len(s) == 1:
            return [s]
        last_zero_start = len(s)-1
        for j in range(len(s)):
            if s[j] != "0":
                last_zero_start = j - 1
                break
        if last_zero_start == len(s) - 1:
            return []
        first_zero_end = 0
        for j in range(len(s)-1, -1, -1):
            if s[j] != "0":
                first_zero_end = j + 1
                break
        if first_zero_end < len(s):
            if last_zero_start >= 0:
                return []
            else:
                return [s]
        if last_zero_start >= 0:
            return ["0." + s[1:]]
        res = [s]
        for j in range(len(s)-1):
            res.append(s[:(j+1)] + "." + s[(j+1):])        
        return res
