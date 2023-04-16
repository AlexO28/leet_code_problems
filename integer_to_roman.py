# convert integer to roman (from 1 to 3999)


class Solution:
    def intToRoman(self, num: int) -> str:
        num_str = ''
        if num >= 3000:
            num_str = 'MMM'
            num = num - 3000
        elif num >= 2000:
            num_str = 'MM'
            num = num - 2000
        elif num >= 1000:
            num_str = 'M'
            num = num - 1000
        if num >= 900:
            num_str += 'CM'
            num -= 900
        elif num >= 800:
            num_str += 'DCCC'
            num -= 800
        elif num >= 700:
            num_str += 'DCC'
            num -= 700
        elif num >= 600:
            num_str += 'DC'
            num -= 600
        elif num >= 500:
            num_str += 'D'
            num -= 500
        elif num >= 400:
            num_str += 'CD'
            num -= 400
        elif num >= 300:
            num_str += 'CCC'
            num -= 300
        elif num >= 200:
            num_str += 'CC'
            num -= 200
        elif num >= 100:
            num_str += 'C'
            num -= 100
        if num >= 90:
            num_str += 'XC'
            num -= 90
        elif num >= 80:
            num_str += 'LXXX'
            num -= 80
        elif num >= 70:
            num_str += 'LXX'
            num -= 70
        elif num >= 60:
            num_str += 'LX'
            num -= 60
        elif num >= 50:
            num_str += 'L'
            num -= 50
        elif num >= 40:
            num_str += 'XL'
            num -= 40
        elif num >= 30:
            num_str += 'XXX'
            num -= 30
        elif num >= 20:
            num_str += 'XX'
            num -= 20
        elif num >= 10:
            num_str += 'X'
            num -= 10
        if num == 9:
            num_str += 'IX'
        elif num == 8:
            num_str += 'VIII'
        elif num == 7:
            num_str += 'VII'
        elif num == 6:
            num_str += 'VI'
        elif num == 5:
            num_str += 'V'
        elif num == 4:
            num_str += 'IV'
        elif num == 3:
            num_str += 'III'
        elif num == 2:
            num_str += 'II'
        elif num == 1:
            num_str += 'I'
        return num_str
