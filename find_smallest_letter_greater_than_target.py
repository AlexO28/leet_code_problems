# You are given an array of characters letters that is sorted in non-decreasing order, and a character target. There are at least two different characters in letters.
# Return the smallest character in letters that is lexicographically greater than target. If such a character does not exist, return the first character in letters.
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        alphabet = list("abcdefghijklmnopqrstuvwxyz")
        if target == "z":
            return letters[0]
        ind = alphabet.index(target)
        for j in range(ind+1, len(alphabet)):
            if alphabet[j] in letters:
                return alphabet[j]
        return letters[0]
