# You are given a phone number as a string number. number consists of digits, spaces ' ', and/or dashes '-'.
# You would like to reformat the phone number in a certain manner. Firstly, remove all spaces and dashes. Then, group the digits from left to right into blocks of length 3 until there are 4 or fewer digits. The final digits are then grouped as follows:
# 2 digits: A single block of length 2.
# 3 digits: A single block of length 3.
# 4 digits: Two blocks of length 2 each.
# The blocks are then joined by dashes. Notice that the reformatting process should never produce any blocks of length 1 and produce at most two blocks of length 2.
Return the phone number after formatting.
class Solution:
    def reformatNumber(self, number: str) -> str:
        number = number.replace(" ", "").replace("-", "")
        groups = []
        numbers = list(number)
        group = []
        for elem in number:
            if len(group) < 3:
                group.append(elem)
            else:
                groups.append(group)
                group = [elem]
        if len(group) > 1:
            groups.append(group)
        else:
            old_group = groups.pop()
            old_group.append(group[0])
            if len(old_group) < 4:
                groups.append(old_group)
            else:
                group_1 = old_group[:2]
                group_2 = old_group[2:]
                groups.append(group_1)
                groups.append(group_2)
        groups = ["".join(group) for group in groups]
        return "-".join(groups)
