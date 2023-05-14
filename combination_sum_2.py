# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.
# Each number in candidates may only be used once in the combination.
# Note: The solution set must not contain duplicate combinations.

def find_results(candidates, target, pos):
    results = []
    for j in range(pos, len(candidates)):
        if (j > pos) and (j < len(candidates) - 1):
            if (candidates[j] == candidates[j - 1]):
                continue
        if candidates[j] == target:
            results.append([candidates[j]])
        elif candidates[j] < target:
            if j < len(candidates) - 1:
                res = find_results(candidates, target - candidates[j], j + 1)
                if len(res) > 0:
                    for elem_res in res:
                        res0 = [candidates[j]]
                        res0.extend(elem_res)
                        results.append(res0)
    return results


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort(reverse=True)
        results = find_results(candidates, target, 0)
        unique_results = []
        for result in results:
            result.sort()
            if result not in unique_results:
                unique_results.append(result)
        return unique_results
