# You are given an array of strings of the same length words.
# In one move, you can swap any two even indexed characters or any two odd indexed characters of a string words[i].
# Two strings words[i] and words[j] are special-equivalent if after any number of moves, words[i] == words[j].
# For example, words[i] = "zzxy" and words[j] = "xyzz" are special-equivalent because we may make the moves "zzxy" -> "xzzy" -> "xyzz".
# A group of special-equivalent strings from words is a non-empty subset of words such that:
# Every pair of strings in the group are special equivalent, and
# The group is the largest size possible (i.e., there is not a string words[i] not in the group such that words[i] is special-equivalent to every string in the group).
# Return the number of groups of special-equivalent strings from words.
class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        group_dict = {}
        for word in words:
            odd_part = []
            even_part = []
            for i in range(len(word)):
                if i % 2 == 0:
                    even_part.append(word[i])
                else:
                    odd_part.append(word[i])
            even_part.sort()
            odd_part.sort()
            phrase = "".join(even_part) + "_" + "".join(odd_part)
            if phrase not in group_dict:
                group_dict[phrase] = 1
        return len(group_dict)
