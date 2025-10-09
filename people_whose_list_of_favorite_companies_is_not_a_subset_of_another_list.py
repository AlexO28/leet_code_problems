# Given the array favoriteCompanies where favoriteCompanies[i] is the list of favorites companies for the ith person (indexed from 0).
# Return the indices of people whose list of favorite companies is not a subset of any other list of favorites companies. You must return the indices in increasing order.
from typing import List


class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        if len(favoriteCompanies) == 1:
            return [0]
        res = []
        for i in range(len(favoriteCompanies)):
            set_A = set(favoriteCompanies[i])
            found = False
            for j in range(len(favoriteCompanies)):
                if i != j:
                    set_B = set(favoriteCompanies[j])
                    if set_A <= set_B:
                        found = True
                        break
            if not found:
                res.append(i)
        return res
