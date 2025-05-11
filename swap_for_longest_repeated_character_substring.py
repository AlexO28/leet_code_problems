# You are given a string text. You can swap two of the characters in the text.
# Return the length of the longest substring with repeated characters.
class Solution:
    def maxRepOpt1(self, text: str) -> int:
        freq_dict = {}
        for elem in text:
            if elem in freq_dict:
                freq_dict[elem] += 1
            else:
                freq_dict[elem] = 1
        max_length = 0
        current_index = 0
        while current_index < len(text):
            start_index = current_index
            while (start_index < len(text)) and (text[start_index] == text[current_index]):
                start_index += 1
            next_index = start_index + 1
            while (next_index < len(text)) and (text[next_index] == text[current_index]):
                next_index += 1
            max_length = max(max_length, min(freq_dict[text[current_index]], next_index - current_index))
            current_index = start_index
        return max_length
