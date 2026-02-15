# Given n cuboids where the dimensions of the ith cuboid is cuboids[i] = [widthi, lengthi, heighti] (0-indexed). Choose a subset of cuboids and place them on each other.
# You can place cuboid i on cuboid j if widthi <= widthj and lengthi <= lengthj and heighti <= heightj. You can rearrange any cuboid's dimensions by rotating it to put it on another cuboid.
# Return the maximum height of the stacked cuboids.
from typing import List


class Solution:
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        for c in cuboids:
            c.sort()
        cuboids.sort()
        f = [0] * len(cuboids)
        for i in range(len(cuboids)):
            for j in range(i):
                if (cuboids[j][1] <= cuboids[i][1]) and (
                    cuboids[j][2] <= cuboids[i][2]
                ):
                    f[i] = max(f[i], f[j])
            f[i] += cuboids[i][2]
        return max(f)
