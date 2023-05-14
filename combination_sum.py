# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.
# The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the 
# frequency
# of at least one of the chosen numbers is different.
# The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.


def find_results(candidates, target, pos):
    results = []
    for j in range(pos, len(candidates)):
        if candidates[j] == target:
            results.append([candidates[j]])
        elif candidates[j] < target:
            res = find_results(candidates, target - candidates[j], pos)
            if len(res) > 0:
                for elem_res in res:
                    res0 = [candidates[j]]
                    res0.extend(elem_res)
                    results.append(res0)
    return results


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort(reverse=True)
        results = find_results(candidates, target, 0)
        unique_results = []
        for result in results:
            result.sort()
            if result not in unique_results:
                unique_results.append(result)
        return unique_results
