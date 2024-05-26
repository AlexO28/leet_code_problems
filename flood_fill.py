# An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.
# You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the pixel image[sr][sc].
# To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with color.
# Return the modified image after performing the flood fill.
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        self.image = image
        if self.image[sr][sc] != color:
            self.flood(sr, sc, color, self.image[sr][sc])
        return self.image

    def flood(self, i, j, col1, col2):
        if self.image[i][j] == col2:
            self.image[i][j] = col1
            if i > 0:
                self.flood(i-1, j, col1, col2)
            if j > 0:
                self.flood(i, j-1, col1, col2)
            if i < len(self.image)-1:
                self.flood(i+1, j, col1, col2)
            if j < len(self.image[0])-1:
                self.flood(i, j+1, col1, col2)
