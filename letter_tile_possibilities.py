# You have n  tiles, where each tile has one letter tiles[i] printed on it.
# Return the number of possible non-empty sequences of letters you can make using the letters printed on those tiles.
from collections import Counter


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        tile_counter = Counter(tiles)
        return self.search(tile_counter)

    def search(self, tile_counter):
        combinations_count = 0
        for tile, count in tile_counter.items():
            if count > 0:
                combinations_count += 1
                tile_counter[tile] -= 1
                combinations_count += self.search(tile_counter)
                tile_counter[tile] += 1
        return combinations_count
