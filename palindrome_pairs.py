# You are given a 0-indexed array of unique strings words.
# Return an array of all the palindrome pairs of words.


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        hashmap = {}
        for j in range(len(words)):
            hashmap[words[j][::-1]] = j
        res = []
        for index in range(len(words)):
            word = words[index]
            if "" in hashmap and index != hashmap[""] and word == word[::-1]:
                res.append([index, hashmap[""]])
            for i in range(1, len(word) + 1):
                left = word[:i]
                right = word[i:]
                if left in hashmap and right == right[::-1] and index != hashmap[left]:
                    res.append([index, hashmap[left]])
                if right in hashmap and left == left[::-1] and index != hashmap[right]:
                    res.append([hashmap[right], index])
        return res
