# You are given a string num, which represents a large integer. You are also given a 0-indexed integer array change of length 10 that maps each digit 0-9 to another digit. More formally, digit d maps to digit change[d].
# You may choose to mutate a single substring of num. To mutate a substring, replace each digit num[i] with the digit it maps to in change (i.e. replace num[i] with change[num[i]]).
# Return a string representing the largest possible integer after mutating (or choosing not to) a single substring of num.
# A substring is a contiguous sequence of characters within the string.
from typing import List


class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        num = list(num)
        res = []
        state = "not found"
        for elem in num:
            elem = int(elem)
            if state == "skip":
                res.append(elem)
            elif state == "not found":
                new_elem = change[elem]
                if new_elem > elem:
                    state = "found"
                    res.append(new_elem)
                else:
                    res.append(elem)
            else:
                new_elem = change[elem]
                if new_elem < elem:
                    state = "skip"
                    res.append(elem)
                else:
                    res.append(new_elem)
        return "".join([str(elem) for elem in res])
