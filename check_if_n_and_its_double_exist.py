# Given an array arr of integers, check if there exist two indices i and j such that :
# i != j
# 0 <= i, j < arr.length
# arr[i] == 2 * arr[j]
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr_dict = {}
        for elem in arr:
            if elem in arr_dict:
                if arr_dict[elem] == 1:
                    arr_dict[elem] = 2
            else:
                arr_dict[elem] = 1
        for i in range(len(arr)):
            if arr[i] == 0:
                if arr_dict[0] > 1:
                    return True
            else:
                if 2*arr[i] in arr_dict:
                    return True
        return False
