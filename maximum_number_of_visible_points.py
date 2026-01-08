# You are given an array points, an integer angle, and your location, where location = [posx, posy] and points[i] = [xi, yi] both denote integral coordinates on the X-Y plane.
# Initially, you are facing directly east from your position. You cannot move from your position, but you can rotate. In other words, posx and posy cannot be changed. Your field of view in degrees is represented by angle, determining how wide you can see from any given view direction. Let d be the amount in degrees that you rotate counterclockwise. Then, your field of view is the inclusive range of angles [d - angle/2, d + angle/2].
# You can see some set of points if, for each point, the angle formed by the point, your position, and the immediate east direction from your position is in your field of view.
# There can be multiple points at one coordinate. There may be points at your location, and you can always see these points regardless of your rotation. Points do not obstruct your vision to other points.
# Return the maximum number of points you can see.
from typing import List
from math import atan2, pi
from bisect import bisect_right


class Solution:
    def visiblePoints(
        self, points: List[List[int]], angle: int, location: List[int]
    ) -> int:
        v = []
        x, y = location
        same = 0
        for xi, yi in points:
            if xi == x and yi == y:
                same += 1
            else:
                v.append(atan2(yi - y, xi - x))
        v.sort()
        v += [deg + 2 * pi for deg in v]
        t = angle * pi / 180
        mx = max((bisect_right(v, v[i] + t) - i for i in range(len(v))), default=0)
        return mx + same
