class Solution:
    def calculate(self, s: str) -> int:
        new_s = ""
        for elem in s:
            if elem == "/":
                new_s += "//"
            else:
                new_s += elem
        return int(eval(new_s))
