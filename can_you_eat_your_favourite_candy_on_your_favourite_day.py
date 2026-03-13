# You are given a (0-indexed) array of positive integers candiesCount where candiesCount[i] represents the number of candies of the ith type you have. You are also given a 2D array queries where queries[i] = [favoriteTypei, favoriteDayi, dailyCapi].
# You play a game with the following rules:
# You start eating candies on day 0.
# You cannot eat any candy of type i unless you have eaten all candies of type i - 1.
# You must eat at least one candy per day until you have eaten all the candies.
# Construct a boolean array answer such that answer.length == queries.length and answer[i] is true if you can eat a candy of type favoriteTypei on day favoriteDayi without eating more than dailyCapi candies on any day, and false otherwise. Note that you can eat different types of candy on the same day, provided that you follow rule 2.
# Return the constructed array answer.
from typing import List


class Solution:
    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        prefixes = [0]
        summa = 0
        for candy in candiesCount:
            summa += candy
            prefixes.append(summa)
        res = []
        for favouriteType, favouriteDay, dailyCap in queries:
            latest_day = prefixes[favouriteType + 1] - 1
            earliest_day = prefixes[favouriteType] // dailyCap
            res.append(earliest_day <= favouriteDay <= latest_day)
        return res
