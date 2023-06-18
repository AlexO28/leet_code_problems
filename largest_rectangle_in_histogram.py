# Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = list()
        max_area = 0
        index = 0
        while index < len(heights):
            if (not stack) or (heights[stack[-1]] <= heights[index]):
                stack.append(index)
                index += 1
            else:
                top_of_stack = stack.pop()
                if stack:
                    area = heights[top_of_stack] * (index - stack[-1] - 1)
                else:    
                    area = heights[top_of_stack] * index
                max_area = max(max_area, area)
        while stack:
            top_of_stack = stack.pop()
            if stack:
                area = heights[top_of_stack] * (index - stack[-1] - 1)
            else:    
                area = heights[top_of_stack] * index
            max_area = max(max_area, area)
        return max_area
