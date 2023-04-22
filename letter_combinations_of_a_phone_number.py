# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
#
# A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        results = []
        if len(digits) == 0:
            return '' 
        data = {'2': 'abc',
                '3': 'def',
                '4': 'ghi',
                '5': 'jkl',
                '6': 'mno',
                '7': 'pqrs',
                '8': 'tuv',
                '9': 'wxyz'}
        for digit in digits:
            digit_list = list(data[digit])
            if len(results) == 0:
                results = digit_list
            else:
                results_new = []
                for j in range(len(results)*len(digit_list)):
                    res_num, digit_num = divmod(j, len(digit_list))
                    results_new.append(results[res_num] + digit_list[digit_num])
                results = results_new
        return results
