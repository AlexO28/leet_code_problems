# implement Levenstain distance between words


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1) == 0:
            return len(word2)
        if len(word2) == 0:
            return len(word1)
        mat = []
        for i in range(len(word1)):
            temp_list = []
            for j in range(len(word2)):
                temp_list.append(0)
            mat.append(temp_list)
        for i in range(len(word1)):
            for j in range(len(word2)):
                if (i == 0) and (j == 0):
                    if (word1[len(word1)-1] != word2[len(word2)-1]):
                        mat[0][0] = 1
                    continue
                if word1[len(word1)-i-1] == word2[len(word2)-j-1]:
                    if (i >= 1) and (j >= 1):
                        mat[i][j] = mat[i-1][j-1]
                    elif i == 0:
                        mat[0][j] = mat[0][j-1] 
                    else:
                        if word2[len(word2)-j-1] in word1[len(word1)-i:]:
                            mat[i][0] = mat[i-1][0] + 1
                        else:
                            mat[i][0] = mat[i-1][0]
                else:
                    if (i >= 1) and (j >= 1):
                        mat[i][j] = 1 + min(mat[i-1][j], mat[i][j-1], mat[i-1][j-1])
                    elif (j == 0):
                        mat[i][0] = 1 + mat[i-1][0]
                    else:
                        mat[0][j] = 1 + mat[0][j-1]
        return mat[len(word1)-1][len(word2)-1]
