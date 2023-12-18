# Given a string s containing an out-of-order English representation of digits 0-9, return the digits in ascending order.
class Solution:
    def originalDigits(self, s: str) -> str:
        number_of_zeros = s.count("z")
        number_of_twos = s.count("w")
        number_of_fours = s.count("u")
        number_of_six = s.count("x")
        number_of_eight = s.count("g")
        number_of_fives = s.count("f") - number_of_fours
        number_of_seven = s.count("s") - number_of_six
        number_of_nines = s.count("i") - number_of_fives - number_of_eight - number_of_six
        number_of_ones = s.count("o") - number_of_zeros - number_of_twos - number_of_fours
        number_of_threes = s.count("h") - number_of_eight
        res = []
        if number_of_zeros > 0:
            res.extend(["0"]*(number_of_zeros))
        if number_of_ones > 0:
            res.extend(["1"]*(number_of_ones))
        if number_of_twos > 0:
            res.extend(["2"]*(number_of_twos))
        if number_of_threes > 0:
            res.extend(["3"]*(number_of_threes))
        if number_of_fours > 0:
            res.extend(["4"]*(number_of_fours))
        if number_of_fives > 0:
            res.extend(["5"]*(number_of_fives))
        if number_of_six > 0:
            res.extend(["6"]*(number_of_six))
        if number_of_seven > 0:
            res.extend(["7"]*(number_of_seven))
        if number_of_eight > 0:
            res.extend(["8"]*(number_of_eight))
        if number_of_nines > 0:
            res.extend(["9"]*(number_of_nines))
        return ''.join(res)
