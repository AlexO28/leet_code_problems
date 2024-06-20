# In the universe Earth C-137, Rick discovered a special form of magnetic force between two balls if they are put in his new invented basket. Rick has n empty baskets, the ith basket is at position[i], Morty has m balls and needs to distribute the balls into the baskets such that the minimum magnetic force between any two balls is maximum.
# Rick stated that magnetic force between two different balls at positions x and y is |x - y|.
# Given the integer array position and the integer m. Return the required force.
class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        self.positions = position
        self.m = m
        left = 1
        right = position[-1] - position[0]      
        while left < right:
            mid = (left + right + 1) // 2
            if self.can_place_balls(mid):
                left = mid
            else:
                right = mid - 1
        return left

    def can_place_balls(self, min_distance):
        previous_position = self.positions[0]
        count = 1
        for current_position in self.positions[1:]:
            if current_position - previous_position >= min_distance:
                previous_position = current_position
                count += 1
        return count >= self.m
