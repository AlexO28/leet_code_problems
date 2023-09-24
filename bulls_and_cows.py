# You are playing the Bulls and Cows game with your friend.
# You write down a secret number and ask your friend to guess what the number is. When your friend makes a guess, you provide a hint with the following info:
# The number of "bulls", which are digits in the guess that are in the correct position.
# The number of "cows", which are digits in the guess that are in your secret number but are located in the wrong position. Specifically, the non-bull digits in the guess that could be rearranged such that they become bulls.
# Given the secret number secret and your friend's guess guess, return the hint for your friend's guess.


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        number_of_bulls = 0
        cows = {}
        for j in range(len(secret)):
            if secret[j] == guess[j]:
                number_of_bulls += 1
            else:
                if guess[j] not in cows.keys():
                    cows[guess[j]] = 1
                else:
                    cows[guess[j]] += 1
        number_of_cows = 0
        for j in range(len(secret)):
            if secret[j] != guess[j]:
                if secret[j] in cows.keys():
                    if cows[secret[j]] > 0:
                        number_of_cows += 1
                        cows[secret[j]] -= 1
        return str(number_of_bulls) + "A" + str(number_of_cows) + "B"
 
