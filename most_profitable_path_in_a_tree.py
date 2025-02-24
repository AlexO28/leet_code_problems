# There is an undirected tree with n nodes labeled from 0 to n - 1, rooted at node 0. You are given a 2D integer array edges of length n - 1 where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree.
# At every node i, there is a gate. You are also given an array of even integers amount, where amount[i] represents:
# the price needed to open the gate at node i, if amount[i] is negative, or,
# the cash reward obtained on opening the gate at node i, otherwise.
# The game goes on as follows:
# Initially, Alice is at node 0 and Bob is at node bob.
# At every second, Alice and Bob each move to an adjacent node. Alice moves towards some leaf node, while Bob moves towards node 0.
# For every node along their path, Alice and Bob either spend money to open the gate at that node, or accept the reward. Note that:
# If the gate is already open, no price will be required, nor will there be any cash reward.
# If Alice and Bob reach the node simultaneously, they share the price/reward for opening the gate there. In other words, if the price to open the gate is c, then both Alice and Bob pay c / 2 each. Similarly, if the reward at the gate is c, both of them receive c / 2 each.
# If Alice reaches a leaf node, she stops moving. Similarly, if Bob reaches node 0, he stops moving. Note that these events are independent of each other.
# Return the maximum net income Alice can have if she travels towards the optimal leaf node.
from typing import List
from collections import defaultdict


class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        self.graph = defaultdict(list)
        self.time_to_reach = [len(edges)+1]*(len(edges)+1)
        for a, b in edges:
            self.graph[a].append(b)
            self.graph[b].append(a)
        self.find_time_to_reach(bob, -1, 0)
        self.time_to_reach[bob] = 0
        self.max_profit = float("-inf")
        self.find_max_profit(0, -1, 0, 0, amount)
        return self.max_profit


    def find_time_to_reach(self, i, prev, t):
        if i == 0:
            self.time_to_reach[0] = min(self.time_to_reach[0], t)
            return True
        else:
            for neighbor in self.graph[i]:
                if (neighbor != prev) and (self.find_time_to_reach(neighbor, i, t+1)):
                    self.time_to_reach[neighbor] = min(self.time_to_reach[neighbor], t+1)
                    return True
            return False      

    def find_max_profit(self, i, prev, t, current_profit, amount):
        if t == self.time_to_reach[i]:
            current_profit += amount[i] // 2
        elif t < self.time_to_reach[i]:
            current_profit += amount[i]
        if (len(self.graph[i]) == 1) and (self.graph[i][0] == prev):
            self.max_profit = max(self.max_profit, current_profit)
        else:
            for neighbor in self.graph[i]:
                if neighbor != prev:
                    self.find_max_profit(neighbor, i, t+1, current_profit, amount)
