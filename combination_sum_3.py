# Find all valid combinations of k numbers that sum up to n such that the following conditions are true:
# Only numbers 1 through 9 are used.
# Each number is used at most once.
# Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        candidates = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        if n > sum(candidates[:k]):
            return []
        results = self.find_results(candidates, n, 0)
        unique_results = []
        for result in results:
            if len(result) == k:
                result.sort()
                if (result not in unique_results):
                    unique_results.append(result)
        return unique_results
        
    def find_results(self, candidates, target, pos):
        results = []
        for j in range(pos, len(candidates)):
            if candidates[j] == target:
                results.append([candidates[j]])
            elif candidates[j] < target:
                if j < len(candidates) - 1:
                    res = self.find_results(candidates, target - candidates[j], j + 1)
                    if len(res) > 0:
                        for elem_res in res:
                            res0 = [candidates[j]]
                            res0.extend(elem_res)
                            results.append(res0)
        return results
