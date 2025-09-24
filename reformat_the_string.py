# You are given an alphanumeric string s. (Alphanumeric string is a string consisting of lowercase English letters and digits).
# You have to find a permutation of the string where no letter is followed by another letter and no digit is followed by another digit. That is, no two adjacent characters have the same type.
# Return the reformatted string or return an empty string if it is impossible to reformat the string.
class Solution:
    def reformat(self, s: str) -> str:
        numbers = "0123456789"
        elements_numbers = []
        elements_letters = []
        for elem in s:
            if elem in numbers:
                elements_numbers.append(elem)
            else:
                elements_letters.append(elem)
        if len(elements_numbers) == len(elements_letters) + 1:
            res = [elements_numbers[0]]
            for j in range(len(elements_letters)):
                res.append(elements_letters[j])
                res.append(elements_numbers[j + 1])
            return "".join(res)
        elif len(elements_numbers) == len(elements_letters):
            res = []
            for j in range(len(elements_letters)):
                res.append(elements_letters[j])
                res.append(elements_numbers[j])
            return "".join(res)
        elif len(elements_letters) == len(elements_numbers) + 1:
            res = [elements_letters[0]]
            for j in range(len(elements_numbers)):
                res.append(elements_numbers[j])
                res.append(elements_letters[j + 1])
            return "".join(res)
        else:
            return ""
