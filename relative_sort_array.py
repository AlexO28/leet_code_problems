# Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.
# Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2. Elements that do not appear in arr2 should be placed at the end of arr1 in ascending order.
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        freq_dict = {}
        for elem in arr1:
            if elem in freq_dict:
                freq_dict[elem] += 1
            else:
                freq_dict[elem] = 1
        res = []
        for elem in arr2:
            if elem in freq_dict.keys():
                res.extend([elem]*freq_dict[elem])
                freq_dict[elem] = 0
        res_extra = []
        for elem in freq_dict.keys():
            val = freq_dict[elem] 
            if val > 0:
                res_extra.extend([elem]*val)
        res_extra.sort()
        res.extend(res_extra)
        return res
