# You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.
# We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.
from math import inf


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        self.times_dict = {}
        for u, v, w in times:
            if u in self.times_dict:
                self.times_dict[u].append([v, w])
            else:
                self.times_dict[u] = [[v, w]]
        self.spread_arr = [inf]*n
        self.spread_arr[k-1] = 0
        self.send_beam(k)
        max_val = max(self.spread_arr)
        if max_val == inf:
            max_val = -1
        return max_val

    def send_beam(self, u):
        if u in self.times_dict:
            for v, w in self.times_dict[u]:
                diff = self.spread_arr[u-1] + w
                if self.spread_arr[v-1] > diff:
                    self.spread_arr[v-1] = diff
                    self.send_beam(v)
