# Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below.
# In the American keyboard:
# the first row consists of the characters "qwertyuiop",
# the second row consists of the characters "asdfghjkl", and
# the third row consists of the characters "zxcvbnm"
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first_row = "qwertyuiop"
        second_row = "asdfghjkl"
        third_row = "zxcvbnm"
        new_words = []
        for i in range(len(words)):
            word = list(set(list(words[i].lower())))
            found = True
            for elem in word:
                if elem not in first_row:
                    found = False
                    break
            if found:
                new_words.append(words[i])
                continue
            found = True
            for elem in word:
                if elem not in second_row:
                    found = False
                    break
            if found:
                new_words.append(words[i])
                continue
            found = True
            for elem in word:
                if elem not in third_row:
                    found = False
                    break
            if found:
                new_words.append(words[i])
                continue
        return new_words
