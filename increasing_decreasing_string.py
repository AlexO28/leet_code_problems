# You are given a string s. Reorder the string using the following algorithm:
# Remove the smallest character from s and append it to the result.
# Remove the smallest character from s that is greater than the last appended character, and append it to the result.
# Repeat step 2 until no more characters can be removed.
# Remove the largest character from s and append it to the result.
# Remove the largest character from s that is smaller than the last appended character, and append it to the result.
# Repeat step 5 until no more characters can be removed.
# Repeat steps 1 through 6 until all characters from s have been removed.
# If the smallest or largest character appears more than once, you may choose any occurrence to append to the result.
# Return the resulting string after reordering s using this algorithm.
class Solution:
    def sortString(self, s: str) -> str:
        freq_dict = {}
        for elem in s:
            if elem in freq_dict:
                freq_dict[elem] += 1
            else:
                freq_dict[elem] = 1
        res = []
        alphabet = list("abcdefghijklmnopqrstuvwxyz")
        while len(freq_dict) > 0:
            for letter in alphabet:
                if letter in freq_dict:
                    res.append(letter)
                    if freq_dict[letter] == 1:
                        del freq_dict[letter]
                    else:
                        freq_dict[letter] -= 1
            alphabet = alphabet[::-1]
        return "".join(res)
