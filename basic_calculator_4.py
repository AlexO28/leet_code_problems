# Given an expression such as expression = "e + 8 - a + 5" and an evaluation map such as {"e": 1} (given in terms of evalvars = ["e"] and evalints = [1]), return a list of tokens representing the simplified expression, such as ["-1*a","14"]
# An expression alternates chunks and symbols, with a space separating each chunk and symbol.
# A chunk is either an expression in parentheses, a variable, or a non-negative integer.
# A variable is a string of lowercase letters (not including digits.) Note that variables can be multiple letters, and note that variables never have a leading coefficient or unary operator like "2x" or "-x".
# Expressions are evaluated in the usual order: brackets first, then multiplication, then addition and subtraction.
# For example, expression = "1 + 2 * 3" has an answer of ["7"].
# The format of the output is as follows:
# For each term of free variables with a non-zero coefficient, we write the free variables within a term in sorted order lexicographically.
# For example, we would never write a term like "b*a*c", only "a*b*c".
# Terms have degrees equal to the number of free variables being multiplied, counting multiplicity. We write the largest degree terms of our answer first, breaking ties by lexicographic order ignoring the leading coefficient of the term.
# For example, "a*a*b*c" has degree 4.
# The leading coefficient of the term is placed directly to the left with an asterisk separating it from the variables (if they exist.) A leading coefficient of 1 is still printed.
# An example of a well-formatted answer is ["-2*a*a*a", "3*a*a*b", "3*b*b", "4*a", "5*c", "-6"].
# Terms (including constant terms) with coefficient 0 are not included.
# For example, an expression of "0" has an output of [].
from collections import Counter


class Solution:
    def basicCalculatorIV(
        self, expression: str, evalvars: List[str], evalints: List[int]
    ) -> List[str]:
        tokens = list(self.__getTokens(expression))
        evalMap = {a: b for a, b in zip(evalvars, evalints)}

        for i, token in enumerate(tokens):
            if token in evalMap:
                tokens[i] = str(evalMap[token])
        postfix = self.__infixToPostfix(tokens)
        return self.__evaluate(postfix).toList()

    def __getTokens(self, s):
        i = 0
        for j, c in enumerate(s):
            if c == " ":
                if i < j:
                    yield s[i:j]
                i = j + 1
            elif c in "()+-*":
                if i < j:
                    yield s[i:j]
                yield c
                i = j + 1
        if i < len(s):
            yield s[i:]

    def __infixToPostfix(self, tokens):
        postfix = []
        ops = []
        for token in tokens:
            if token == "(":
                ops.append(token)
            elif token == ")":
                while ops[-1] != "(":
                    postfix.append(ops.pop())
                ops.pop()
            elif token in "+-*":
                while ops and self.__precedes(ops[-1], token):
                    postfix.append(ops.pop())
                ops.append(token)
            else:
                postfix.append(token)
        return postfix + ops[::-1]

    def __precedes(self, prevOp, currOp):
        if prevOp == "(":
            return False
        return prevOp == "*" or currOp in "+-"

    def __evaluate(self, postfix):
        polys = []
        for token in postfix:
            if token in "+-*":
                b = polys.pop()
                a = polys.pop()
                if token == "+":
                    polys.append(a + b)
                elif token == "-":
                    polys.append(a - b)
                else:
                    polys.append(a * b)
            elif token.lstrip("-").isnumeric():
                polys.append(Poly("1", int(token)))
            else:
                polys.append(Poly(token, 1))
        return polys[0]


class Poly:
    def __init__(self, term=None, coef=None):
        if term and coef:
            self.terms = collections.Counter({term: coef})
        else:
            self.terms = collections.Counter()

    def __add__(self, other):
        for term, coef in other.terms.items():
            self.terms[term] += coef
        return self

    def __sub__(self, other):
        for term, coef in other.terms.items():
            self.terms[term] -= coef
        return self

    def __mul__(self, other):
        res = Poly()
        for a, aCoef in self.terms.items():
            for b, bCoef in other.terms.items():
                res.terms[self.__merge(a, b)] += aCoef * bCoef
        return res

    def toList(self):
        for term in list(self.terms.keys()):
            if not self.terms[term]:
                del self.terms[term]
        terms = list(self.terms.keys())
        terms.sort(key=self.__cmp)
        return [self.__concat(term) for term in terms]

    def __cmp(self, term):
        if term == "1":
            return (0,)
        return (-len(term.split("*")), term)

    def __concat(self, term):
        if term == "1":
            return str(self.terms[term])
        return str(self.terms[term]) + "*" + term

    def __merge(self, a, b):
        if a == "1":
            return b
        if b == "1":
            return a
        res = []
        A = a.split("*")
        B = b.split("*")
        i = 0
        j = 0
        while i < len(A) and j < len(B):
            if A[i] < B[j]:
                res.append(A[i])
                i += 1
            else:
                res.append(B[j])
                j += 1
        return "*".join(res + A[i:] + B[j:])
