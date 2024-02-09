# Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        reverse = True
        res = []
        for sum_dir in range(0, len(mat) + len(mat[0]) +1):
            if reverse:
                for i in range(len(mat)-1, -1, -1):
                    j = sum_dir - i
                    if (j >= 0) and (j < len(mat[0])): 
                        res.append(mat[i][j])
                reverse = False
            else:
                for i in range(len(mat)):
                    j = sum_dir - i
                    if (j >= 0) and (j < len(mat[0])): 
                        res.append(mat[i][j])
                    reverse = True
        return res
