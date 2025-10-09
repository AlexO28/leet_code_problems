# Given a sentence text (A sentence is a string of space-separated words) in the following format:
# First letter is in upper case.
# Each word in text are separated by a single space.
# Your task is to rearrange the words in text such that all words are rearranged in an increasing order of their lengths. If two words have the same length, arrange them in their original order.
# Return the new text following the format shown above.
from functools import cmp_to_key


class Solution:
    def arrangeWords(self, text: str) -> str:

        def compare(x, y):
            if len(x) > len(y):
                return 1
            elif len(x) < len(y):
                return -1
            else:
                return x < y

        text = " ".join(sorted(text.lower().split(" "), key=cmp_to_key(compare)))
        return text[0].upper() + text[1:]
