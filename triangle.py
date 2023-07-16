# Given a triangle array, return the minimum path sum from top to bottom.
# For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        totals = triangle[0]
        if len(triangle) > 1:
            for i in range(1, len(triangle)):
                new_totals = []
                new_totals.append(totals[0] + triangle[i][0])
                for j in range(1, len(totals)):
                    if totals[j] > totals[j-1]:
                        new_totals.append(totals[j-1] + triangle[i][j])
                    else:
                        new_totals.append(totals[j] + triangle[i][j])
                new_totals.append(totals[-1] + triangle[i][-1])
                totals = new_totals
        return min(totals)
