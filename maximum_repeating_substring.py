# For a string sequence, a string word is k-repeating if word concatenated k times is a substring of sequence. The word's maximum k-repeating value is the highest value k where word is k-repeating in sequence. If word is not a substring of sequence, word's maximum k-repeating value is 0.
# Given strings sequence and word, return the maximum k-repeating value of word in sequence.
class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        if len(word) > len(sequence):
            return 0
        else:
            max_k = len(sequence) // len(word)
            for k in range(max_k, 0, -1):
                if word * k in sequence:
                    return k
            return 0
