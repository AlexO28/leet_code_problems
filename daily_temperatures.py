# Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if len(temperatures) == 1:
            return [0]
        res = [0]*len(temperatures)
        stack = []
        for j in range(len(temperatures)):
            while (len(stack) > 0):
                if temperatures[j] <= temperatures[stack[-1]]:
                    break
                index = stack.pop()
                res[index] = j - index
            stack.append(j)
        return res
