# Given a string formula representing a chemical formula, return the count of each atom.
# The atomic element always starts with an uppercase character, then zero or more lowercase letters, representing the name.
# One or more digits representing that element's count may follow if the count is greater than 1. If the count is 1, no digits will follow.
# For example, "H2O" and "H2O2" are possible, but "H1O2" is impossible.
# Two formulas are concatenated together to produce another formula.
# For example, "H2O2He3Mg4" is also a formula.
# A formula placed in parentheses, and a count (optionally added) is also a formula.
# For example, "(H2O2)" and "(H2O2)3" are formulas.
# Return the count of all elements as a string in the following form: the first name (in sorted order), followed by its count (if that count is more than 1), followed by the second name (in sorted order), followed by its count (if that count is more than 1), and so on.
from collections import Counter


class Solution:
    def countOfAtoms(self, formula: str) -> str:        
        count = self.parseFormula(formula)
        res = []
        for atom, num in sorted(count.items()):
            if num == 1:
                res.append(atom)
            else:
                res.append(atom + str(num))
        return "".join(res)

    def parseFormula(self, formula):
        count = Counter()
        if len(formula) == 0:
            return count
        i = 0
        while i < len(formula):
            if formula[i].isalpha():
                atom = formula[i]
                atomNum = []
                i += 1
                while i < len(formula) and formula[i].isalpha() and formula[i].islower():
                    atom += formula[i]
                    i += 1
                while i < len(formula) and formula[i].isdigit():
                    atomNum.append(formula[i])
                    i += 1
                if len(atomNum) == 0:
                    count[atom] += 1
                else:
                    atomNum = int("".join(atomNum))
                    count[atom] += atomNum
            elif formula[i] == "(":
                left = i
                parent = 1 
                while i < len(formula) and parent != 0:
                    i += 1
                    if formula[i] == "(":
                        parent += 1
                    elif formula[i] == ")":
                        parent -= 1
                right = i
                i += 1
                atomNum = []
                while i < len(formula) and formula[i].isdigit():
                    atomNum.append(formula[i])
                    i += 1
                if len(atomNum) == 0:
                    atomNum = 1
                else:
                    atomNum = int("".join(atomNum))
                innerCount = self.parseFormula(formula[left + 1 : right])
                for c, n in innerCount.items():
                    count[c] += n * atomNum
        count += self.parseFormula(formula[i + 1 :])
        return count
