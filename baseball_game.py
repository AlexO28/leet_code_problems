# You are keeping the scores for a baseball game with strange rules. At the beginning of the game, you start with an empty record.
# You are given a list of strings operations, where operations[i] is the ith operation you must apply to the record and is one of the following:
# An integer x.
# Record a new score of x.
# '+'.
# Record a new score that is the sum of the previous two scores.
# 'D'.
# Record a new score that is the double of the previous score.
# 'C'.
# Invalidate the previous score, removing it from the record.
# Return the sum of all the scores on the record after applying all the operations.
# The test cases are generated such that the answer and all intermediate calculations fit in a 32-bit integer and that all operations are valid.
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        self.arr = []
        for oper in operations:
            if oper == "C":
                self.arr.pop()
            elif oper == "D":
                self.arr.append(2*self.arr[-1])
            elif oper == "+":
                self.arr.append(self.arr[-1] + self.arr[-2])
            else:
                self.arr.append(int(oper))
        return sum(self.arr)
