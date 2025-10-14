# Given an array of strings names of size n. You will create n folders in your file system such that, at the ith minute, you will create a folder with the name names[i].
# Since two files cannot have the same name, if you enter a folder name that was previously used, the system will have a suffix addition to its name in the form of (k), where, k is the smallest positive integer such that the obtained name remains unique.
# Return an array of strings of length n where ans[i] is the actual name the system will assign to the ith folder when you create it.
from typing import List
from collections import defaultdict


class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        name_counter = defaultdict(int)
        for i, name in enumerate(names):
            if name in name_counter:
                suffix_num = name_counter[name]
                while name + "(" + str(suffix_num) + ")" in name_counter:
                    suffix_num += 1
                name_counter[name] = suffix_num + 1
                names[i] = name + "(" + str(suffix_num) + ")"
            name_counter[names[i]] = 1
        return names
