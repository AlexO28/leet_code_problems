# Given an integer array arr of distinct integers and an integer k.
# A game will be played between the first two elements of the array (i.e. arr[0] and arr[1]). In each round of the game, we compare arr[0] with arr[1], the larger integer wins and remains at position 0, and the smaller integer moves to the end of the array. The game ends when an integer wins k consecutive rounds.
# Return the integer which will win the game.
# It is guaranteed that there will be a winner of the game.

class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if k >= len(arr):
            return max(arr)
        number_of_wins = 0
        while True:
            if arr[0] > arr[1]:
                number_of_wins += 1
                save = arr[1]
                del arr[1]
                arr.append(save)
            else:
                number_of_wins = 1
                save = arr[0]
                del arr[0]
                arr.append(save)
            if number_of_wins == k:
                return arr[0]
