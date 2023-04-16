# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
#
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
#
# Return the maximum amount of water a container can store.

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left_index = 0
        right_index = len(height)-1
        max_water = 0
        while right_index > left_index:
            temp_water = min(height[left_index], height[right_index])*(right_index-left_index)
            max_water = max(max_water, temp_water)
            if height[left_index] <= height[right_index]:
                left_index += 1
            else:
                right_index -= 1
        return max_water
