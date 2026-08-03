# You are given a 2D integer array items where items[i] = [pricei, beautyi] denotes the price and beauty of an item respectively.
# You are also given a 0-indexed integer array queries. For each queries[j], you want to determine the maximum beauty of an item whose price is less than or equal to queries[j]. If no such item exists, then the answer to this query is 0.
# Return an array answer of the same length as queries where answer[j] is the answer to the jth query.
import bisect
from typing import List


class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()
        beauty_data = {}
        max_val = -1
        for price, beauty in items:
            max_val = max(max_val, beauty)
            beauty_data[price] = max_val
        keys = list(beauty_data.keys())
        res = [] 
        for query in queries:
            ind = bisect.bisect_right(keys, query)
            if ind == 0:
                res.append(0)
            else:
                res.append(beauty_data[keys[ind - 1]])
        return res
