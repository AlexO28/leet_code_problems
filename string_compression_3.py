# Given a string word, compress it using the following algorithm:
# Begin with an empty string comp. While word is not empty, use the following operation:
# Remove a maximum length prefix of word made of a single character c repeating at most 9 times.
# Append the length of the prefix followed by c to comp.
# Return the string comp.
class Solution:
    def compressedString(self, word: str) -> str:
        new_line = []
        start = 0
        while start < len(word):
            elem = word[start]
            count = 0
            while word[start] == elem:
                count += 1
                start += 1
                if start == len(word):
                    break
                if count == 9:
                    break
            new_line.append(str(count))
            new_line.append(elem)
        return "".join(new_line)
