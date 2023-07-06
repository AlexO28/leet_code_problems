# Given an integer numRows, return the first numRows of Pascal's triangle.

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for j in range(numRows):
            if j == 0:
                res.append([1])
            else:
                row = []
                for i in range(j+1):
                    if i == 0:
                        row.append(res[j-1][0])
                    elif i == j:
                        row.append(res[j-1][j-1])
                    else:
                        row.append(res[j-1][i-1] + res[j-1][i])
                res.append(row)
        return res
