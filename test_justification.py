# Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.
# You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.
# Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.
# For the last line of text, it should be left-justified, and no extra space is inserted between words.


def form_str_by_adding_whitespaces(line_list, line_len, max_len):
    nevyazka = max_len - line_len
    if len(line_list) == 1:
        return line_list[0] + ' '*nevyazka
    min_whitespaces, difference = divmod(nevyazka, len(line_list) - 1)
    whitespaces = [min_whitespaces]*(len(line_list) - 1)
    for j in range(len(whitespaces)):
        if difference == 0:
            break
        whitespaces[j] += 1
        difference -= 1
    line_str = line_list[0]
    for j in range(len(whitespaces)):
        line_str += ' '*(whitespaces[j]) + line_list[j + 1]
    return line_str


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        lines = []
        line_list = []
        line_len = 0
        for word in words:
            if line_len + len(line_list) + len(word) <= maxWidth:
                line_len += len(word)
                line_list.append(word)
            else:
                line_str = form_str_by_adding_whitespaces(line_list, line_len, maxWidth)
                lines.append(line_str)
                line_list = [word]
                line_len = len(word)
        line_str = form_str_by_adding_whitespaces(line_list, line_len, maxWidth)
        lines.append(line_str)
        last_line_list = lines[-1].split(' ')
        last_line_list = [word for word in last_line_list if word != '']
        last_line = ' '.join(last_line_list)
        nevyazka = maxWidth - len(last_line)
        if nevyazka > 0:
            last_line += ' '*(nevyazka)
        lines[-1] = last_line
        return lines
