# You are playing a game that contains multiple characters, and each of the characters has two main properties: attack and defense. You are given a 2D integer array properties where properties[i] = [attacki, defensei] represents the properties of the ith character in the game.
# A character is said to be weak if any other character has both attack and defense levels strictly greater than this character's attack and defense levels. More formally, a character i is said to be weak if there exists another character j where attackj > attacki and defensej > defensei.
# Return the number of weak characters.
from typing import List


class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        number_of_weak_characters = 0
        properties.sort(key=lambda x: (-x[0], x[1]))
        max_defense = 0
        for _, defense in properties:
            if defense < max_defense:
                number_of_weak_characters += 1
            max_defense = max(max_defense, defense)
        return number_of_weak_characters
