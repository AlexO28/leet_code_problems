# Solve a given equation and return the value of 'x' in the form of a string "x=#value". The equation contains only '+', '-' operation, the variable 'x' and its coefficient. You should return "No solution" if there is no solution for the equation, or "Infinite solutions" if there are infinite solutions for the equation.
# If there is exactly one solution for the equation, we ensure that the value of 'x' is an integer.
class Solution:
    def solveEquation(self, equation: str) -> str:
        left_part, right_part = equation.split("=")
        a_left, b_left = self.parseEquationPart(left_part)
        a_right, b_right = self.parseEquationPart(right_part)
        if a_left == a_right:
            if b_left == b_right:
                return "Infinite solutions"
            else:
                return "No solution"
        else:
            return "x=" + str(int((b_right-b_left)/(a_left-a_right)))
        
    def parseEquationPart(self, part):
        i = 0
        a = 0
        b = 0
        to_add = True
        if part[0] == "-":
            to_add = False
            i += 1
        elif part[0] == "+":
            i += 1
        j = i
        while i < len(part):
            if j == len(part):
                termType, term = self.parseTerm(part[i:j])
                if to_add:
                    if termType == 1:
                        a += int(term)
                    else:
                        b += int(term)
                else:
                    if termType == 1:
                        a -= int(term)
                    else:
                        b -= int(term)
                break
            elif (part[j] == "+") or (part[j] == "-"):
                termType, term = self.parseTerm(part[i:j])
                if to_add:
                    if termType == 1:
                        a += int(term)
                    else:
                        b += int(term)
                else:
                    if termType == 1:
                        a -= int(term)
                    else:
                        b -= int(term)
                to_add = (part[j] == "+")
                i = j+1
                j = i
            else:
                j += 1
        return a, b 

    def parseTerm(self, term):
        if "x" in term:
            if term == "x":
                return 1, 1
            else:
                return 1, term[:-1]
        else:
            return 0, term
