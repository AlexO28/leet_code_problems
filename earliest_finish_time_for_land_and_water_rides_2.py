# You are given two categories of theme park attractions: land rides and water rides.
# Land rides
# landStartTime[i] – the earliest time the ith land ride can be boarded.
# landDuration[i] – how long the ith land ride lasts.
# Water rides
# waterStartTime[j] – the earliest time the jth water ride can be boarded.
# waterDuration[j] – how long the jth water ride lasts.
# A tourist must experience exactly one ride from each category, in either order.
# A ride may be started at its opening time or any later moment.
# If a ride is started at time t, it finishes at time t + duration.
# Immediately after finishing one ride the tourist may board the other (if it is already open) or wait until it opens.
# Return the earliest possible time at which the tourist can finish both rides.
from typing import List
import bisect
import numpy as np
from math import inf


class Solution:
    def earliestFinishTime(
        self,
        landStartTime: List[int],
        landDuration: List[int],
        waterStartTime: List[int],
        waterDuration: List[int],
    ) -> int:
        landStartTime = np.array(landStartTime)
        landDuration = np.array(landDuration)
        waterStartTime = np.array(waterStartTime)
        waterDuration = np.array(waterDuration)
        land_indices = np.argsort(landStartTime)
        water_indices = np.argsort(waterStartTime)
        landStartTime = landStartTime[land_indices]
        landDuration = landDuration[land_indices]
        waterStartTime = waterStartTime[water_indices]
        waterDuration = waterDuration[water_indices]
        curval = inf
        land_prefixes = []
        for duration in landDuration:
            curval = min(curval, duration)
            land_prefixes.append(curval)
        curval = inf
        water_prefixes = []
        for duration in waterDuration:
            curval = min(curval, duration)
            water_prefixes.append(curval)
        curval = inf
        land_suffixes = []
        for j in range(len(landDuration) - 1, -1, -1):
            curval = min(curval, landStartTime[j] + landDuration[j])
            land_suffixes.append(curval)
        curval = inf
        water_suffixes = []
        for j in range(len(waterDuration) - 1, -1, -1):
            curval = min(curval, waterStartTime[j] + waterDuration[j])
            water_suffixes.append(curval)
        water_suffixes = water_suffixes[::-1]
        land_suffixes = land_suffixes[::-1]
        res = inf
        for j in range(len(landStartTime)):
            finish1 = landStartTime[j] + landDuration[j]
            ind = bisect.bisect_right(waterStartTime, finish1)
            if 0 < ind < len(water_prefixes):
                res = min(finish1 + water_prefixes[ind - 1], water_suffixes[ind], res)
            elif ind > 0:
                res = min(finish1 + water_prefixes[ind - 1], res)
            else:
                res = min(water_suffixes[ind], res)
        for j in range(len(waterStartTime)):
            finish1 = waterStartTime[j] + waterDuration[j]
            ind = bisect.bisect_right(landStartTime, finish1)
            if 0 < ind < len(land_prefixes):
                res = min(finish1 + land_prefixes[ind - 1], land_suffixes[ind], res)
            elif ind > 0:
                res = min(finish1 + land_prefixes[ind - 1], res)
            else:
                res = min(land_suffixes[ind], res)
        return int(res)
