# You are given a string s and an array of strings words. All the strings of words are of the same length.
# A concatenated substring in s is a substring that contains all the strings of any permutation of words concatenated.
#
#For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are all concatenated strings. "acdbef" is not a concatenated substring because it is not the concatenation of any permutation of words.
#Return the starting indices of all the concatenated substrings in s. You can return the answer in any order.

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_count = {}
        for word in words:
            if word not in word_count.keys():
                word_count[word] = 1
            else:
                word_count[word] += 1
        str_len = len(words[0]) * len(words)
        results = []
        for pos in range(len(s) - str_len + 1):
            candidate = s[pos:(pos + str_len)]
            check_map = {}
            for j in range(len(words)):
                check_word = candidate[j*len(words[0]):((j+1)*len(words[0]))]
                if check_word not in check_map.keys():
                    check_map[check_word] = 1
                else:
                    check_map[check_word] += 1
            if check_map == word_count:
                results.append(pos)
        return results
