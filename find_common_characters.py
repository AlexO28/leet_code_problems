# Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        if len(words) == 1:
            return words[0]
        freq_dict_common = self.form_freq_dict(words[0])
        for word in words:
            freq_dict = self.form_freq_dict(word)
            freq_dict_next = {}
            for elem in freq_dict_common:
                if elem in freq_dict:
                    freq_dict_next[elem] = min(freq_dict_common[elem], freq_dict[elem])
            freq_dict_common = freq_dict_next
            if len(freq_dict_common.keys()) == 0:
                return ""
        resstr = []
        for elem in freq_dict_common.keys():
            resstr.extend([elem]*freq_dict_common[elem])
        return resstr
        
    def form_freq_dict(self, line):
        freq_dict = {}
        for elem in line:
            if elem in freq_dict:
                freq_dict[elem] += 1
            else:
                freq_dict[elem] = 1
        return freq_dict
