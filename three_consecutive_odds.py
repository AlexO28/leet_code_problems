# Given an integer array arr, return true if there are three consecutive odd numbers in the array. Otherwise, return false.
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        number_of_odds = 0
        for elem in arr:
            if elem % 2 == 0:
                number_of_odds = 0
            else:
                number_of_odds += 1
            if number_of_odds == 3:
                return True
        return False
