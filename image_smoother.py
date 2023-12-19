# An image smoother is a filter of the size 3 x 3 that can be applied to each cell of an image by rounding down the average of the cell and the eight surrounding cells (i.e., the average of the nine cells in the blue smoother). If one or more of the surrounding cells of a cell is not present, we do not consider it in the average (i.e., the average of the four cells in the red smoother).
class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        res = []
        for i in range(len(img)):
            temp_arr = []
            for j in range(len(img[0])):
                temp_arr.append(0)
            res.append(temp_arr)
        for i in range(len(img)):
            for j in range(len(img[0])):
                val = img[i][j]
                count = 1
                if (i > 0) & (j > 0):
                    val += img[i-1][j-1]
                    count += 1
                if i > 0:
                    val += img[i-1][j]
                    count += 1
                if (i > 0) & (j < len(img[0])-1):
                    val += img[i-1][j+1]
                    count += 1
                if (i < len(img)-1) & (j < len(img[0])-1):
                    val += img[i+1][j+1]
                    count += 1
                if j < len(img[0])-1:
                    val += img[i][j+1]
                    count += 1
                if (i < len(img)-1) & (j > 0):
                    val += img[i+1][j-1]
                    count += 1
                if j > 0:
                    val += img[i][j-1]
                    count += 1
                if i < len(img)-1:
                    val += img[i+1][j]
                    count += 1
                res[i][j] = int(val/count)
        return res
 
