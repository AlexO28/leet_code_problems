# You are given two images, img1 and img2, represented as binary, square matrices of size n x n. A binary matrix has only 0s and 1s as values.
# We translate one image however we choose by sliding all the 1 bits left, right, up, and/or down any number of units. We then place it on top of the other image. We can then calculate the overlap by counting the number of positions that have a 1 in both images.
# Return the largest possible overlap.
class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        overlap_counter = {}
        for i in range(len(img1)):
            for j in range(len(img2)):
                if img1[i][j] == 1:
                    for h in range(len(img1)):
                        for k in range(len(img2)):
                            if img2[h][k] == 1:
                                pair = str(i-h) + "_" + str(j-k)
                                if pair in overlap_counter:
                                    overlap_counter[pair] += 1
                                else:
                                    overlap_counter[pair] = 1
        if len(overlap_counter) == 0:
            return 0
        else:
            return max(overlap_counter.values())
