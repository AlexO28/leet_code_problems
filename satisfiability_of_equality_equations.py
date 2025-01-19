# You are given an array of strings equations that represent relationships between variables where each string equations[i] is of length 4 and takes one of two different forms: "xi==yi" or "xi!=yi".Here, xi and yi are lowercase letters (not necessarily different) that represent one-letter variable names.
# Return true if it is possible to assign integers to variable names so as to satisfy all the given equations, or false otherwise.
from typing import List


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        self.parent = list(range(26))
        a_code = ord("a")
        for equation in equations:
            if equation[1] == "=":
                self.parent[self.find(ord(equation[0]) - a_code)] = self.find(ord(equation[-1]) - a_code)
        for equation in equations:
            if equation[1] == "!":
                if self.find(ord(equation[0]) - a_code) == self.find(ord(equation[-1]) - a_code):
                    return False
        return True

    def find(self, x):
        if self.parent[x] != x:
           self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
