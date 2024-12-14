# Given a wordlist, we want to implement a spellchecker that converts a query word into a correct word.
# For a given query word, the spell checker handles two categories of spelling mistakes:
# Capitalization: If the query matches a word in the wordlist (case-insensitive), then the query word is returned with the same case as the case in the wordlist.
# Vowel Errors: If after replacing the vowels ('a', 'e', 'i', 'o', 'u') of the query word with any vowel individually, it matches a word in the wordlist (case-insensitive), then the query word is returned with the same case as the match in the wordlist.
# In addition, the spell checker operates under the following precedence rules:
# When the query exactly matches a word in the wordlist (case-sensitive), you should return the same word back.
# When the query matches a word up to capitlization, you should return the first such match in the wordlist.
# When the query matches a word up to vowel errors, you should return the first such match in the wordlist.
# If the query has no matches in the wordlist, you should return the empty string.
# Given some queries, return a list of words answer, where answer[i] is the correct word for query = queries[i].
from typing import List
import re


class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        res = []
        words_small = [word.lower() for word in wordlist]
        words_star = [re.sub("a|e|i|o|u", "*", word) for word in words_small]
        for query in queries:
            found = False
            for j in range(len(wordlist)):
                if query == wordlist[j]:
                    found = True
                    res.append(wordlist[j])
                    break
            if not found:
                query_small = query.lower()
                for j in range(len(wordlist)):
                    if query_small == words_small[j]:
                        res.append(wordlist[j])
                        found = True
                        break
            if not found:
                query_star = re.sub("a|e|i|o|u", "*", query_small)
                for j in range(len(wordlist)):
                    if query_star == words_star[j]:
                        res.append(wordlist[j])
                        found = True
                        break
            if not found:
                res.append("")
        return res
