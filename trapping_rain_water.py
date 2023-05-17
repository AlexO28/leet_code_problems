# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.


class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 1:
            return 0
        left = 0
        right = len(height)-1
        l_max = 0
        r_max = 0
        result = 0
        while (left <= right):  
            if r_max <= l_max:  
                result += max(0, r_max-height[right])
                r_max = max(r_max, height[right])
                right -= 1
            else:  
                result += max(0, l_max-height[left])
                l_max = max(l_max, height[left])
                left += 1
        return result
