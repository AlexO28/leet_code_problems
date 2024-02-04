# You are given an integer array nums. Two players are playing a game with this array: player 1 and player 2.
# Player 1 and player 2 take turns, with player 1 starting first. Both players start the game with a score of 0. At each turn, the player takes one of the numbers from either end of the array (i.e., nums[0] or nums[nums.length - 1]) which reduces the size of the array by 1. The player adds the chosen number to their score. The game ends when there are no more elements in the array.
# Return true if Player 1 can win the game. If the scores of both players are equal, then player 1 is still the winner, and you should also return true. You may assume that both players are playing optimally.
class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        if len(nums) <= 2:
            return True
        return self.predict(nums, 0, True)

    def predict(self, nums, rel, result):
        if len(nums) == 3:
            if result:
                first_wins = (nums[1] <= nums[0] + nums[2] + rel)
            else:
                first_wins = (nums[1] + rel <= nums[0] + nums[2])
            return first_wins
        for j in range(2):
            if j == 0:
                new_rel = nums[-1]
            else:
                new_rel = nums[0]
            if result:
                check = self.predict(nums[j:(len(nums)+j-1)], rel+new_rel, False)
            else:
                check = self.predict(nums[j:(len(nums)+j-1)], rel-new_rel, True)
            if result:
                if check:
                    return True
            else:
                if not check:
                    return False
        return not result
