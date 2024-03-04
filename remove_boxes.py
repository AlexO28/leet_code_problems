# You are given several boxes with different colors represented by different positive numbers.
# You may experience several rounds to remove boxes until there is no box left. Each time you can choose some continuous boxes with the same color (i.e., composed of k boxes, k >= 1), remove them and get k * k points.
# Return the maximum points you can get.
from functools import cache


class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        self.boxes = boxes
        return self.dfs(0, len(boxes) - 1, 0)
 
    @cache
    def dfs(self, start, end, continuous_count):
        if start > end:
            return 0
        while start < end and self.boxes[end] == self.boxes[end - 1]:
            end -= 1
            continuous_count += 1
        score = self.dfs(start, end - 1, 0) + (continuous_count + 1) ** 2
        for middle in range(start, end):
            if self.boxes[middle] == self.boxes[end]:
                score = max(score, self.dfs(middle + 1, end - 1, 0) + self.dfs(start, middle, continuous_count + 1))
        return score
