# You are given a string text of words that are placed among some number of spaces. Each word consists of one or more lowercase English letters and are separated by at least one space. It's guaranteed that text contains at least one word.
# Rearrange the spaces so that there is an equal number of spaces between every pair of adjacent words and that number is maximized. If you cannot redistribute all the spaces equally, place the extra spaces at the end, meaning the returned string should be the same length as text.
# Return the string after rearranging the spaces.
class Solution:
    def reorderSpaces(self, text: str) -> str:
        words = []
        num_spaces = 0
        cur_word = []
        text = list(text)
        for elem in text:
            if elem == " ":
                num_spaces += 1
                if len(cur_word) > 0:
                    cur_word = "".join(cur_word)
                    words.append(cur_word)
                    cur_word = []
            else:
                cur_word.append(elem)
        if len(cur_word) > 0:
            cur_word = "".join(cur_word)
            words.append(cur_word)
            cur_word = []
        if len(words) == 1:
            remainder = num_spaces
        else:
            main_part, remainder = divmod(num_spaces, len(words) - 1)
        new_line = []
        for j in range(len(words)):
            new_line.append(words[j])
            if j == len(words) - 1:
                new_line.append(" " * remainder)
            else:
                new_line.append(" " * main_part)
        return "".join(new_line)
