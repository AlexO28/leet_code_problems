# In a warehouse, there is a row of barcodes, where the ith barcode is barcodes[i].
# Rearrange the barcodes so that no two adjacent barcodes are equal. You may return any answer, and it is guaranteed an answer exists.
from typing import List
import numpy as np


class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        freq_dict = {}
        for element in barcodes:
            if element in freq_dict:
                freq_dict[element] += 1
            else:
                freq_dict[element] = 1
        values = np.array(list(freq_dict.values()))
        keys = np.array(list(freq_dict.keys()))
        keys = keys[values.argsort()[::-1]]
        pos = 0
        res = [None]*(len(barcodes))
        key_pos = 0
        while key_pos < len(keys):
            if freq_dict[keys[key_pos]] > 0:
                res[pos] = int(keys[key_pos])
                freq_dict[keys[key_pos]] -= 1
                pos += 2
                if pos >= len(barcodes):
                    pos = 1
            else:
                key_pos += 1
        return res
