# You are given a series of video clips from a sporting event that lasted time seconds. These video clips can be overlapping with each other and have varying lengths.
# Each video clip is described by an array clips where clips[i] = [starti, endi] indicates that the ith clip started at starti and ended at endi.
# We can cut these clips into segments freely.
# Return the minimum number of clips needed so that we can cut the clips into segments that cover the entire sporting event [0, time]. If the task is impossible, return -1.
from typing import List


class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        furthest_reach = [0]*(time)
        for start, end in clips:
            if start < time:
                furthest_reach[start] = max(furthest_reach[start], end)
        clips_required = 0
        current_end = 0
        next_end = 0
        for second in range(time):
            next_end = max(next_end, furthest_reach[second])
            if next_end <= second:
                return -1
            elif current_end == second:
                clips_required += 1
                current_end = next_end
        return clips_required
