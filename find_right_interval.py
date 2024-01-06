# You are given an array of intervals, where intervals[i] = [starti, endi] and each starti is unique.
# The right interval for an interval i is an interval j such that startj >= endi and startj is minimized. Note that i may equal j.
# Return an array of right interval indices for each interval i. If no right interval exists for interval i, then put -1 at index i.
class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        intervals_new = intervals.copy()
        intervals_new.sort(key=lambda interval: interval[0])
        freq_dict = {}
        for i in range(len(intervals_new)):
            found = False
            for j in range(i, len(intervals_new)):
                if intervals_new[j][0] >= intervals_new[i][1]:
                    found = True
                    freq_dict[self.list_to_str(intervals_new[i])] = j
                    break
            if not found:
                freq_dict[self.list_to_str(intervals_new[i])] = -1
        res = []
        freq_dict_original = {}
        for i in range(len(intervals)):
            freq_dict_original[self.list_to_str(intervals[i])] = i
        for i in range(len(intervals)):
            ind = freq_dict[self.list_to_str(intervals[i])]
            if ind >= 0:
                res.append(freq_dict_original[self.list_to_str(intervals_new[ind])])
            else:
                res.append(-1)
        return res

    def list_to_str(self, interval):
        return str(interval[0]) + "_" + str(interval[1])
