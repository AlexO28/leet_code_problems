# You are given a 0-indexed binary string floor, which represents the colors of tiles on a floor:
# floor[i] = '0' denotes that the ith tile of the floor is colored black.
# On the other hand, floor[i] = '1' denotes that the ith tile of the floor is colored white.
# You are also given numCarpets and carpetLen. You have numCarpets black carpets, each of length carpetLen tiles. Cover the tiles with the given carpets such that the number of white tiles still visible is minimum. Carpets may overlap one another.
# Return the minimum number of white tiles still visible.
from functools import cache


class Solution:
    def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        self.floor = floor
        self.s = [0] * (len(self.floor) + 1)
        for i, c in enumerate(floor):
            self.s[i + 1] = self.s[i] + int(c == "1")
        ans = self.search(0, numCarpets, carpetLen)
        self.search.cache_clear()
        return ans

    @cache
    def search(self, i, j, carpetLen):
        if i >= len(self.floor):
            return 0
        elif self.floor[i] == "0":
            return self.search(i + 1, j, carpetLen)
        elif j == 0:
            return self.s[-1] - self.s[i]
        else:
            return min(
                1 + self.search(i + 1, j, carpetLen),
                self.search(i + carpetLen, j - 1, carpetLen),
            )
