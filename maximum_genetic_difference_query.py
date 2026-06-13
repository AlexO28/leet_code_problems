# There is a rooted tree consisting of n nodes numbered 0 to n - 1. Each node's number denotes its unique genetic value (i.e. the genetic value of node x is x). The genetic difference between two genetic values is defined as the bitwise-XOR of their values. You are given the integer array parents, where parents[i] is the parent for node i. If node x is the root of the tree, then parents[x] == -1.
# You are also given the array queries where queries[i] = [nodei, vali]. For each query i, find the maximum genetic difference between vali and pi, where pi is the genetic value of any node that is on the path between nodei and the root (including nodei and the root). More formally, you want to maximize vali XOR pi.
# Return an array ans where ans[i] is the answer to the ith query.
from typing import List
from collections import defaultdict


class Solution:
    def maxGeneticDifference(
        self, parents: List[int], queries: List[List[int]]
    ) -> List[int]:
        self.tree = defaultdict(list)
        root = -1
        for child, p in enumerate(parents):
            if p == -1:
                root = child
            else:
                self.tree[p].append(child)
        self.qmap = defaultdict(list)
        for idx, (node, val) in enumerate(queries):
            self.qmap[node].append((val, idx))
        self.ans = [0] * len(queries)
        self.trie = Trie()
        self.search(root)
        return self.ans

    def search(self, u):
        self.trie.insert(u)
        for val, idx in self.qmap[u]:
            self.ans[idx] = self.trie.maxXor(val)
        for v in self.tree[u]:
            self.search(v)
        self.trie.remove(u)


class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0


class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.L = 20

    def insert(self, num):
        node = self.root
        for i in reversed(range(self.L)):
            bit = (num >> i) & 1
            if bit not in node.children:
                node.children[bit] = TrieNode()
            node = node.children[bit]
            node.count += 1

    def remove(self, num):
        node = self.root
        for i in reversed(range(self.L)):
            bit = (num >> i) & 1
            node = node.children[bit]
            node.count -= 1

    def maxXor(self, num):
        node = self.root
        xor = 0
        for i in reversed(range(self.L)):
            bit = (num >> i) & 1
            toggled = 1 - bit
            if toggled in node.children and node.children[toggled].count > 0:
                xor |= 1 << i
                node = node.children[toggled]
            elif bit in node.children and node.children[bit].count > 0:
                node = node.children[bit]
            else:
                break
        return xor
