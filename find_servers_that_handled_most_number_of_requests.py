# You have k servers numbered from 0 to k-1 that are being used to handle multiple requests simultaneously. Each server has infinite computational capacity but cannot handle more than one request at a time. The requests are assigned to servers according to a specific algorithm:
# The ith (0-indexed) request arrives.
# If all servers are busy, the request is dropped (not handled at all).
# If the (i % k)th server is available, assign the request to that server.
# Otherwise, assign the request to the next available server (wrapping around the list of servers and starting from 0 if necessary). For example, if the ith server is busy, try to assign the request to the (i+1)th server, then the (i+2)th server, and so on.
# You are given a strictly increasing array arrival of positive integers, where arrival[i] represents the arrival time of the ith request, and another array load, where load[i] represents the load of the ith request (the time it takes to complete). Your goal is to find the busiest server(s). A server is considered busiest if it handled the most number of requests successfully among all the servers.
# Return a list containing the IDs (0-indexed) of the busiest server(s). You may return the IDs in any order.
from typing import List
from sortedcontainers import SortedList
from heapq import heappop


class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        free = SortedList(range(k))
        busy = []
        cnt = [0] * k
        for i, (start, t) in enumerate(zip(arrival, load)):
            while busy and busy[0][0] <= start:
                free.add(busy[0][1])
                heappop(busy)
            if not free:
                continue
            j = free.bisect_left(i % k)
            if j == len(free):
                j = 0
            server = free[j]
            cnt[server] += 1
            heappush(busy, (start + t, server))
            free.remove(server)
        mx = max(cnt)
        return [i for i, v in enumerate(cnt) if v == mx]
