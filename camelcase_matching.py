# Given an array of strings queries and a string pattern, return a boolean array answer where answer[i] is true if queries[i] matches pattern, and false otherwise.
# A query word queries[i] matches pattern if you can insert lowercase English letters into the pattern so that it equals the query. You may insert a character at any position in pattern or you may choose not to insert any characters at all.
from typing import List


class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        return [self.matchesPattern(query, pattern) for query in queries]

    def matchesPattern(self, query, pattern):
        pattern_index = 0
        query_index = 0
        while pattern_index < len(pattern):
            while (query_index < len(query)) and (query[query_index] != pattern[pattern_index]) and (query[query_index].islower() == True):
                query_index += 1
            if (query_index == len(query)) or (query[query_index] != pattern[pattern_index]):
                return False
            query_index += 1
            pattern_index += 1
        while (query_index < len(query)) and (query[query_index].islower() == True):
            query_index += 1
        return query_index == len(query)
