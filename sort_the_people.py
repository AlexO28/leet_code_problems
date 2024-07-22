import numpy as np


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        return np.array(names)[np.array(heights).argsort()][::-1]
