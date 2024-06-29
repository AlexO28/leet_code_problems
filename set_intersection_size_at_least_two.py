# You are given a 2D integer array intervals where intervals[i] = [starti, endi] represents all the integers from starti to endi inclusively.
# A containing set is an array nums where each interval from intervals has at least two integers in nums.
# Return the minimum possible size of a containing set.
class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[1], -x[0]))
        start = -1
        end = -1
        res = 0
        for current_start, current_end in intervals:
            if current_start > start:
                if current_start > end:
                    res += 2
                    start = current_end - 1
                    end = current_end
                else:
                    res += 1
                    start = end
                    end = current_end
        return res
