# You are given an integer array pref of size n. Find and return the array arr of size n that satisfies:
# pref[i] = arr[0] ^ arr[1] ^ ... ^ arr[i].
# Note that ^ denotes the bitwise-xor operation.


class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        if len(pref) == 1:
            return pref
        arr = [pref[0]]
        for j in range(1, len(pref)):
            arr.append(pref[j-1] ^ pref[j])
        return arr
  
