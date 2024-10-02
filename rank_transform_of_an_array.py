# Given an array of integers arr, replace each element with its rank.
# The rank represents how large the element is. The rank has the following rules:
# Rank is an integer starting from 1.
# The larger the element, the larger the rank. If two elements are equal, their rank must be the same.
# Rank should be as small as possible.
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        temp = list(set(arr))
        temp.sort()
        temp_dict = {temp[j]:(j+1) for j in range(len(temp))}
        return [temp_dict[elem] for elem in arr]
