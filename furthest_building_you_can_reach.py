# You are given an integer array heights representing the heights of buildings, some bricks, and some ladders.
# You start your journey from building 0 and move to the next building by possibly using bricks or ladders.
# While moving from building i to building i+1 (0-indexed),
# If the current building's height is greater than or equal to the next building's height, you do not need a ladder or bricks.
# If the current building's height is less than the next building's height, you can either use one ladder or (h[i+1] - h[i]) bricks.
# Return the furthest building index (0-indexed) you can reach if you use the given ladders and bricks optimally.
import bisect

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        if len(heights) == 1:
            return 0
        sum_of_jumps = 0
        largest_jumps = []
        for j in range(1, len(heights)):
            jump_size = heights[j] - heights[j-1]
            if jump_size > 0:
                if len(largest_jumps) < ladders:
                    bisect.insort(largest_jumps, jump_size)
                else:
                    if len(largest_jumps) > 0:
                        bisect.insort(largest_jumps, jump_size)
                        min_jump = largest_jumps[0]
                        sum_of_jumps += min_jump
                        del largest_jumps[0]
                    else:
                        sum_of_jumps += jump_size
                    if sum_of_jumps > bricks:
                        return j-1
        return len(heights)-1
