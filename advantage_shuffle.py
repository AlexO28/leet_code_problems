# You are given two integer arrays nums1 and nums2 both of the same length. The advantage of nums1 with respect to nums2 is the number of indices i for which nums1[i] > nums2[i].
# Return any permutation of nums1 that maximizes its advantage with respect to nums2.
import numpy as np


class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        freq_dict = {}
        for num in nums1:
            if num in freq_dict:
                freq_dict[num] += 1
            else:
                freq_dict[num] = 1
        indices = np.argsort(nums2)
        permutations = []
        keys = list(freq_dict.keys())
        keys.sort()
        key_index = 0
        found = True
        for index in indices:
            while keys[key_index] <= nums2[index]:
                key_index += 1
                if key_index == len(keys):
                    found = False
                    break
            if not found:
                break
            permutations.append(keys[key_index])
            if freq_dict[keys[key_index]] > 1:
                freq_dict[keys[key_index]] -= 1
            else:
                del freq_dict[keys[key_index]]
                key_index += 1
            if key_index == len(keys):
                break
        for key in freq_dict.keys():
            permutations.extend([key]*(freq_dict[key]))
        perm_dict = {indices[j]:permutations[j] for j in range(len(indices))}
        keys = list(perm_dict.keys())
        keys.sort()
        return [perm_dict[key] for key in keys]
