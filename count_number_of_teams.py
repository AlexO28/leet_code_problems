# There are n soldiers standing in a line. Each soldier is assigned a unique rating value.
# You have to form a team of 3 soldiers amongst them under the following rules:
# Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j], rating[k]).
# A team is valid if: (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k]) where (0 <= i < j < k < n).
# Return the number of teams you can form given the conditions. (soldiers can be part of multiple teams).
class Solution:
    def numTeams(self, rating: List[int]) -> int:
        res = 0
        for i in range(len(rating)):
            left = sum(x < rating[i] for x in rating[:i])
            right = sum(x > rating[i] for x in rating[i + 1:])
            res += left * right
            res += (i - left) * (len(rating) - i - 1 - right)
        return res
