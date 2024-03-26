# Given two arrays of strings list1 and list2, find the common strings with the least index sum.
# A common string is a string that appeared in both list1 and list2.
# A common string with the least index sum is a common string such that if it appeared at list1[i] and list2[j] then i + j should be the minimum value among all the other common strings.
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        freq_dict_1 = {}
        for j in range(len(list1)):
            if list1[j] not in freq_dict_1:
                freq_dict_1[list1[j]] = j
        freq_dict_2 = {}
        for j in range(len(list2)):
            if list2[j] not in freq_dict_2:
                freq_dict_2[list2[j]] = j
        keys = [key for key in freq_dict_1.keys() if key in freq_dict_2.keys()]
        if len(keys) == 0:
            return []
        res = []
        min_val = len(list1) + len(list2) + 1
        for key in keys:
            cur_val = freq_dict_1[key] + freq_dict_2[key]
            if cur_val < min_val:
                min_val = cur_val
                res = [key]
            elif cur_val == min_val:
                res.append(key) 
        return res
