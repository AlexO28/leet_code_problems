# You are given a 2D integer array tiles where tiles[i] = [li, ri] represents that every tile j in the range li <= j <= ri is colored white.
# You are also given an integer carpetLen, the length of a single carpet that can be placed anywhere.
# Return the maximum number of white tiles that can be covered by the carpet.
from typing import List


class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        tiles.sort()
        s = 0
        ans = 0
        j = 0
        for i, (li, ri) in enumerate(tiles):
            while j < len(tiles) and tiles[j][1] - li + 1 <= carpetLen:
                s += tiles[j][1] - tiles[j][0] + 1
                j += 1
            if j < len(tiles) and li + carpetLen > tiles[j][0]:
                ans = max(ans, s + li + carpetLen - tiles[j][0])
            else:
                ans = max(ans, s)
            s -= ri - li + 1
        return ans
