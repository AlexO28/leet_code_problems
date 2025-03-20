# Design an algorithm that accepts a stream of characters and checks if a suffix of these characters is a string of a given array of strings words.
# Implement the StreamChecker class:
# StreamChecker(String[] words) Initializes the object with the strings array words.
# boolean query(char letter) Accepts a new character from the stream and returns true if any non-empty suffix from the stream forms a word that is in words.
from typing import List


class StreamChecker:

    def __init__(self, words: List[str]):
        self.words = words
        self.stream = ""

    def query(self, letter: str) -> bool:
        self.stream += letter
        for word in self.words:
            if len(word) <= len(self.stream):
                if self.stream[-len(word):] == word:
                    return True
        return False
