# You are given an integer n denoting the total number of servers and a 2D 0-indexed integer array logs, where logs[i] = [server_id, time] denotes that the server with id server_id received a request at time time.
# You are also given an integer x and a 0-indexed integer array queries.
# Return a 0-indexed integer array arr of length queries.length where arr[i] represents the number of servers that did not receive any requests during the time interval [queries[i] - x, queries[i]].
# Note that the time intervals are inclusive.
from typing import List
from collections import Counter


class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        cnt = Counter()
        logs.sort(key=lambda x: x[1])
        res = [0] * len(queries)
        j = 0
        k = 0
        for right, i in sorted(zip(queries, count())):
            left = right - x
            while (k < len(logs)) and (logs[k][1] <= right):
                cnt[logs[k][0]] += 1
                k += 1
            while (j < len(logs)) and (logs[j][1] < left):
                cnt[logs[j][0]] -= 1
                if cnt[logs[j][0]] == 0:
                    cnt.pop(logs[j][0])
                j += 1
            res[i] = n - len(cnt)
        return res
