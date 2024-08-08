# Given an array of strings words where each word can be written as a concatenation of the Morse code of each letter.
# Return the number of different transformations among all words we have.
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        MORSE_CODES = {
            "a": ".-",
            "b": "-...",
            "c": "-.-.",
            "d": "-..",
            "e": ".",
            "f": "..-.",
            "g": "--.",
            "h": "....",
            "i": "..",
            "j": ".---",
            "k": "-.-",
            "l": ".-..",
            "m": "--",
            "n": "-.",
            "o": "---",
            "p": ".--.",
            "q": "--.-",
            "r": ".-.",
            "s": "...",
            "t": "-",
            "u": "..-",
            "v": "...-",
            "w": ".--",
            "x": "-..-",
            "y": "-.--",
            "z": "--.."}
        res = []
        for word in words:
            line = "".join([MORSE_CODES[letter] for letter in word])
            res.append(line)
        return len(set(res))
