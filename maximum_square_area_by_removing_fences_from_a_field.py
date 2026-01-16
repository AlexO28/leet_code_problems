# There is a large (m - 1) x (n - 1) rectangular field with corners at (1, 1) and (m, n) containing some horizontal and vertical fences given in arrays hFences and vFences respectively.
# Horizontal fences are from the coordinates (hFences[i], 1) to (hFences[i], n) and vertical fences are from the coordinates (1, vFences[i]) to (m, vFences[i]).
# Return the maximum area of a square field that can be formed by removing some fences (possibly none) or -1 if it is impossible to make a square field.
# Since the answer may be large, return it modulo 109 + 7.
# Note: The field is surrounded by two horizontal fences from the coordinates (1, 1) to (1, n) and (m, 1) to (m, n) and two vertical fences from the coordinates (1, 1) to (m, 1) and (1, n) to (m, n). These fences cannot be removed.
from typing import List


class Solution:
    def maximizeSquareArea(
        self, m: int, n: int, hFences: List[int], vFences: List[int]
    ) -> int:
        hDifferences = self.calculate_differences(hFences, m)
        vDifferences = self.calculate_differences(vFences, n)
        differences = list(hDifferences & vDifferences)
        if len(differences) == 0:
            return -1
        else:
            differences.sort()
            return (differences[-1] ** 2) % 1000000007

    def calculate_differences(self, arr, m):
        arr.append(1)
        arr.append(m)
        arr = list(set(arr))
        arr.sort()
        differences = []
        for i in range(len(arr) - 1):
            for j in range(i + 1, len(arr)):
                differences.append(arr[j] - arr[i])
        differences = set(differences)
        return differences
