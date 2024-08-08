# Sometimes people repeat letters to represent extra feeling. For example:
# "hello" -> "heeellooo"
# "hi" -> "hiiii"
# In these strings like "heeellooo", we have groups of adjacent letters that are all the same: "h", "eee", "ll", "ooo".
# You are given a string s and an array of query strings words. A query word is stretchy if it can be made to be equal to s by any number of applications of the following extension operation: choose a group consisting of characters c, and add some number of characters c to the group so that the size of the group is three or more.
# For example, starting with "hello", we could do an extension on the group "o" to get "hellooo", but we cannot get "helloo" since the group "oo" has a size less than three. Also, we could do another extension like "ll" -> "lllll" to get "helllllooo". If s = "helllllooo", then the query word "hello" would be stretchy because of these two extension operations: query = "hello" -> "hellooo" -> "helllllooo" = s.
# Return the number of query strings that are stretchy.
class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        number_of_stretch_lines = 0
        freqs_s = self.calculate_frequencies(s)
        for word in words:
            freqs_w = self.calculate_frequencies(word)
            if self.compare_frequencies(freqs_s, freqs_w):
                number_of_stretch_lines += 1
        return number_of_stretch_lines

    def calculate_frequencies(self, s):
        freqs = []
        if len(s) == 1:
            return [[s[0], 1]]
        else:
            cur_elem = s[0]
            cur_len = 1
            for j in range(1, len(s)):
                if s[j] == cur_elem:
                    cur_len += 1
                else:
                    freqs.append([cur_elem, cur_len])
                    cur_elem = s[j]
                    cur_len = 1
        freqs.append([cur_elem, cur_len])
        return freqs

    def compare_frequencies(self, freqs1, freqs2):
        if len(freqs2) != len(freqs1):
            return False
        for j in range(len(freqs1)):
            if freqs1[j][0] != freqs2[j][0]:
                return False
            if freqs2[j][1] > freqs1[j][1]:
                return False
            if (freqs1[j][1] < 3) and (freqs2[j][1] < freqs1[j][1]):
                return False
        return True
