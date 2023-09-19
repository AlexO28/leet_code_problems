# Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return the researcher's h-index.

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        cit_dict = {}
        max_val = 0
        for j in range(len(citations)):
            if citations[j] in cit_dict.keys():
                cit_dict[citations[j]].append(j)
            else:
                cit_dict[citations[j]] = [j]
            max_val = max(max_val, citations[j])
        if max_val == 0:
            return 0
        h_index = max_val
        remainder = 0
        while h_index > 0:
            if h_index in cit_dict.keys():
                if len(cit_dict[h_index]) + remainder >= h_index:
                    return h_index
                else:
                    remainder += len(cit_dict[h_index])
            else:
                if remainder >= h_index:
                    return h_index
            h_index -= 1
        return h_index
