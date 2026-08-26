# You are given a binary string s and a positive integer k.
# A substring of s is beautiful if the number of 1's in it is exactly k.
# Let len be the length of the shortest beautiful substring.
# Return the lexicographically smallest beautiful substring of string s with length equal to len. If s doesn't contain a beautiful substring, return an empty string.
# A string a is lexicographically larger than a string b (of the same length) if in the first position where a and b differ, a has a character strictly larger than the corresponding character in b.
class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        candidate_string = ""
        for i in range(len(s) - k + 1):
            num_of_ones = 0
            for j in range(i, len(s)):
                if s[j] == "1":
                    num_of_ones += 1
                    if num_of_ones == k:
                        if candidate_string == "":
                            candidate_string = s[i:(j+1)]
                        else:
                            new_candidate = s[i:(j+1)]
                            if len(new_candidate) < len(candidate_string):
                                candidate_string = new_candidate
                            elif len(new_candidate) == len(candidate_string):
                                candidate_string = min(candidate_string, new_candidate)
        return candidate_string
