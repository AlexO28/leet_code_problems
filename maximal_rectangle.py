# Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        maxArea = 0
        hasZero = False
        hasOne = False
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "1":
                    hasOne = True
                else:
                    hasZero = True
                if hasOne and hasZero:
                    break
            if hasOne and hasZero:
                break
        if hasOne and (not hasZero):
            return len(matrix) * len(matrix[0])
        elif hasZero and (not hasOne):
            return 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "1":
                    tempArea = 0
                    tempWidth = len(matrix[0])
                    for i1 in range(i, len(matrix)):
                        j1 = j
                        while j1 < tempWidth:
                            if matrix[i1][j1] == "0":
                                tempWidth = j1
                                break
                            j1 += 1
                        candidateArea = (i1 - i + 1) * (tempWidth - j)
                        if candidateArea < tempArea:
                            continue
                        else:
                            tempArea = candidateArea
                    if maxArea < tempArea:
                        maxArea = tempArea
        return maxArea
