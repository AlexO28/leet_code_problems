# Your country has an infinite number of lakes. Initially, all the lakes are empty, but when it rains over the nth lake, the nth lake becomes full of water. If it rains over a lake that is full of water, there will be a flood. Your goal is to avoid floods in any lake.
# Given an integer array rains where:
# rains[i] > 0 means there will be rains over the rains[i] lake.
# rains[i] == 0 means there are no rains this day and you can choose one lake this day and dry it.
# Return an array ans where:
# ans.length == rains.length
# ans[i] == -1 if rains[i] > 0.
# ans[i] is the lake you choose to dry in the ith day if rains[i] == 0.
# If there are multiple valid answers return any of them. If it is impossible to avoid flood return an empty array.
# Notice that if you chose to dry a full lake, it becomes empty, but if you chose to dry an empty lake, nothing changes.
from typing import List
from sortedcontainers import SortedList


class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        result = [-1] * (len(rains))
        sunny_days = SortedList()
        last_rain_day = {}
        for day, lake in enumerate(rains):
            if lake > 0:
                if lake in last_rain_day:
                    sunny_day_idx = sunny_days.bisect_right(last_rain_day[lake])
                    if sunny_day_idx == len(sunny_days):
                        return []
                    dry_day = sunny_days[sunny_day_idx]
                    result[dry_day] = lake
                    sunny_days.discard(dry_day)
                last_rain_day[lake] = day
            else:
                sunny_days.add(day)
                result[day] = 1
        return result
