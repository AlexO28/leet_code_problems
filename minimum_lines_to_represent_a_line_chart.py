# You are given a 2D integer array stockPrices where stockPrices[i] = [dayi, pricei] indicates the price of the stock on day dayi is pricei. A line chart is created from the array by plotting the points on an XY plane with the X-axis representing the day and the Y-axis representing the price and connecting adjacent points. One such example is shown below:
# Return the minimum number of lines needed to represent the line chart.
from math import gcd


class Solution:
    def minimumLines(self, stockPrices: list[list[int]]) -> int:
        if len(stockPrices) == 1:
            return 0
        if len(stockPrices) == 2:
            return 1
        stockPrices.sort()
        prev_numerator, prev_denominator = self.calculate_slope_info(
            stockPrices[1][1], stockPrices[0][1], stockPrices[1][0], stockPrices[0][0]
        )
        num_segments = 1
        for i in range(2, len(stockPrices)):
            numerator, denominator = self.calculate_slope_info(
                stockPrices[i][1],
                stockPrices[i - 1][1],
                stockPrices[i][0],
                stockPrices[i - 1][0],
            )
            if (numerator != prev_numerator) or (denominator != prev_denominator):
                prev_numerator = numerator
                prev_denominator = denominator
                num_segments += 1
        return num_segments

    def calculate_slope_info(self, a, b, c, d):
        prev_numerator = a - b
        prev_denominator = c - d
        prev_gcd = gcd(prev_numerator, prev_denominator)
        return prev_numerator / prev_gcd, prev_denominator / prev_gcd
