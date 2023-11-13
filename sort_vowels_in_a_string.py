# Given a 0-indexed string s, permute s to get a new string t such that:
# All consonants remain in their original places. More formally, if there is an index i with 0 <= i < s.length such that s[i] is a consonant, then t[i] = s[i].
# The vowels must be sorted in the nondecreasing order of their ASCII values. More formally, for pairs of indices i, j with 0 <= i < j < s.length such that s[i] and s[j] are vowels, then t[i] must not have a higher ASCII value than t[j].
# Return the resulting string.
# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in lowercase or uppercase. Consonants comprise all letters that are not vowels.


class Solution:
    def sortVowels(self, s: str) -> str:
        VOWELS_LIST = ['A', 'E', 'I', 'O', 'U',
                       'a', 'e', 'i', 'o', 'u']
        vowels_dict = {}
        s = list(s)
        for elem in s:
            if elem in VOWELS_LIST:
                if elem in vowels_dict.keys():
                    vowels_dict[elem] += 1
                else:
                    vowels_dict[elem] = 1
        vowels = list(vowels_dict.keys())
        vowels.sort()
        ind = 0
        res = []
        for elem in s:
            if elem in VOWELS_LIST:
                if vowels_dict[vowels[ind]] == 0:
                    ind += 1
                vowels_dict[vowels[ind]] -= 1
                res.append(vowels[ind])
            else:
                res.append(elem)
        return ''.join(res)
 
