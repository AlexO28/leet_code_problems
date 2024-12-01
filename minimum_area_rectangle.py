# You are given an array of points in the X-Y plane points where points[i] = [xi, yi].
# Return the minimum area of a rectangle formed from these points, with sides parallel to the X and Y axes. If there is not any such rectangle, return 0.
class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        x_dict = {}
        y_dict = {}
        for x, y in points:
            if x in x_dict:
                x_dict[x].append(y)
            else:
                x_dict[x] = [y]
            if y in y_dict:
                y_dict[y].append(x)
            else:
                y_dict[y] = [x]
        min_area = None
        for x in list(x_dict.keys()):
            if len(x_dict[x]) > 1:
                for i in range(len(x_dict[x])-1):
                    for j in range(i+1, len(x_dict[x])):
                        y1 = x_dict[x][i]
                        y2 = x_dict[x][j]
                        intersection = [elem for elem in y_dict[y1] if elem in y_dict[y2]]
                        if len(intersection) > 0:
                            min_delta = None
                            for a in range(len(intersection)):
                                if intersection[a] != x:
                                    if min_delta is None:
                                        min_delta = abs(x - intersection[a])
                                    else:
                                        min_delta = min(min_delta, abs(x - intersection[a]))
                            if min_delta is not None:
                                if min_area is None:
                                    min_area = min_delta * abs(y2 - y1)
                                else:
                                    min_area = min(min_area, min_delta * abs(y2 - y1))
        if min_area is None:
            return 0
        else:
            return min_area
