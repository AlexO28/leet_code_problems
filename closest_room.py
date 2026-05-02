# There is a hotel with n rooms. The rooms are represented by a 2D integer array rooms where rooms[i] = [roomIdi, sizei] denotes that there is a room with room number roomIdi and size equal to sizei. Each roomIdi is guaranteed to be unique.
# You are also given k queries in a 2D array queries where queries[j] = [preferredj, minSizej]. The answer to the jth query is the room number id of a room such that:
# The room has a size of at least minSizej, and
# abs(id - preferredj) is minimized, where abs(x) is the absolute value of x.
# If there is a tie in the absolute difference, then use the room with the smallest such id. If there is no such room, the answer is -1.
# Return an array answer of length k where answer[j] contains the answer to the jth query.
from typing import List
from sortedcontainers import SortedList


class Solution:
    def closestRoom(
        self, rooms: List[List[int]], queries: List[List[int]]
    ) -> List[int]:
        rooms.sort(key=lambda x: x[1])
        idx = sorted(range(len(queries)), key=lambda i: queries[i][1])
        ans = [-1] * len(queries)
        i = 0
        sl = SortedList(x[0] for x in rooms)
        for j in idx:
            prefer, minSize = queries[j]
            while i < len(rooms) and rooms[i][1] < minSize:
                sl.remove(rooms[i][0])
                i += 1
            if i == len(rooms):
                break
            p = sl.bisect_left(prefer)
            if p < len(sl):
                ans[j] = sl[p]
            if p and (ans[j] == -1 or ans[j] - prefer >= prefer - sl[p - 1]):
                ans[j] = sl[p - 1]
        return ans
