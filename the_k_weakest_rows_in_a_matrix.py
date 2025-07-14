# You are given an m x n binary matrix mat of 1's (representing soldiers) and 0's (representing civilians). The soldiers are positioned in front of the civilians. That is, all the 1's will appear to the left of all the 0's in each row.
# A row i is weaker than a row j if one of the following is true:
# The number of soldiers in row i is less than the number of soldiers in row j.
# Both rows have the same number of soldiers and i < j.
# Return the indices of the k weakest rows in the matrix ordered from weakest to strongest.
from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        data = []
        for i in range(len(mat)):
            summa = 0
            for j in range(len(mat[0])):
                if mat[i][j] == 1:
                    summa += 1
                else:
                    break
            data.append((summa, i))
        data.sort()
        return [elem[1] for elem in data][:k]
