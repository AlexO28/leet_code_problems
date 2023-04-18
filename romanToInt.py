# Turn Roman number from 1 to 3999 to int.

class Solution:
    def romanToInt(self, s: str) -> int:
        num_of_thousands = 0
        num_of_hundreds = 0
        num_of_tens = 0
        num_of_units = 0
        if 'MMM' in s:
            num_of_thousands = 3
            s = s.replace('MMM', '')
        elif 'MM' in s:
            num_of_thousands = 2
            s = s.replace('MM', '')
        elif 'M' in s:
            if 'CM' in s:
                num_of_hundreds = 9
                s = s.replace('CM', '')
            if 'M' in s:
                num_of_thousands = 1
                s = s.replace('M', '')
        if 'CM' in s:
            num_of_hundreds = 9
            s = s.replace('CM', '')
        elif 'DCCC' in s:
            num_of_hundreds = 8
            s = s.replace('DCCC', '')
        elif 'DCC' in s:
            num_of_hundreds = 7
            s = s.replace('DCC', '')
        elif 'DC' in s:
            num_of_hundreds = 6
            s = s.replace('DC', '')
        elif 'CD' in s:
            num_of_hundreds = 4
            s = s.replace('CD', '')
        elif 'D' in s:
            num_of_hundreds = 5
            s = s.replace('D', '')
        elif 'CCC' in s:
            num_of_hundreds = 3
            s = s.replace('CCC', '')
        elif 'CC' in s:
            num_of_hundreds = 2
            s = s.replace('CC', '')
        elif 'C' in s:
            if 'XC' in s:
                num_of_tens = 9
                s = s.replace('XC', '')
            if 'C' in s:
                num_of_hundreds = 1
                s = s.replace('C', '')
        if 'XC' in s:
            num_of_tens = 9
            s = s.replace('XC', '')
        elif 'LXXX' in s:
            num_of_tens = 8
            s = s.replace('LXXX', '')
        elif 'LXX' in s:
            num_of_tens = 7
            s = s.replace('LXX', '')
        elif 'LX' in s:
            num_of_tens = 6
            s = s.replace('LX', '')
        elif 'XL' in s:
            num_of_tens = 4
            s = s.replace('XL', '')
        elif 'L' in s:
            num_of_tens = 5
            s = s.replace('L', '')
        elif 'XXX' in s:
            num_of_tens = 3
            s = s.replace('XXX', '')
        elif 'XX' in s:
            num_of_tens = 2
            s = s.replace('XX', '')
        elif 'X' in s:
            if 'IX' in s:
                num_of_units = 9
                s = s.replace('IX', '')
            if 'X' in s:
                num_of_tens = 1
                s = s.replace('X', '')
        if 'IX' in s:
            num_of_units = 9
            s = s.replace('IX', '')
        elif 'VIII' in s:
            num_of_units = 8
            s = s.replace('VIII', '')
        elif 'VII' in s:
            num_of_units = 7
            s = s.replace('VII', '')
        elif 'VI' in s:
            num_of_units = 6
            s = s.replace('VI', '')
        elif 'IV' in s:
            num_of_units = 4
            s = s.replace('IV', '')
        elif 'V' in s:
            num_of_units = 5
            s = s.replace('V', '')
        elif 'III' in s:
            num_of_units = 3
            s = s.replace('III', '')
        elif 'II' in s:
            num_of_units = 2
            s = s.replace('II', '')
        elif 'I' in s:
            num_of_units = 1
            s = s.replace('I', '')
        return num_of_thousands*1000 + num_of_hundreds*100 + num_of_tens*10 + num_of_units
