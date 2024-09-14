# Two strings, X and Y, are considered similar if either they are identical or we can make them equivalent by swapping at most two letters (in distinct positions) within the string X.
# We are given a list strs of strings where every string in strs is an anagram of every other string in strs. How many groups are there?
class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        if len(strs) == 1:
            return 1
        groups = {}
        for i in range(len(strs)):
            for j in range(i, len(strs)):
                if self.are_in_the_same_group(strs[i], strs[j]):
                    if (i in groups) and (j in groups):
                        if groups[i] > groups[j]:
                            min_val = groups[j]
                            max_val = groups[i]
                        else:
                            min_val = groups[i]
                            max_val = groups[j]
                        groups[i] = min_val
                        groups[j] = min_val
                        for group in groups:
                            if groups[group] == max_val:
                                groups[group] = min_val
                    elif i in groups:
                        groups[j] = groups[i]
                    elif j in groups:
                        groups[i] = groups[j]
                    else:
                        groups[j] = i
                        groups[i] = i
        return len(list(set(list(groups.values()))))
    

    def are_in_the_same_group(self, str1, str2):
        num_discrepancies = 0
        inds = []
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                num_discrepancies += 1
                inds.append(i)
                if num_discrepancies > 2:
                    return False
        if num_discrepancies == 0:
            return True
        else:
            return (str1[inds[0]] == str2[inds[1]]) and (str1[inds[1]] == str2[inds[0]])
