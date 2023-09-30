# Given a string num that contains only digits and an integer target, return all possibilities to insert the binary operators '+', '-', and/or '*' between the digits of num so that the resultant expression evaluates to the target value.

# Note that operands in the returned expressions should not contain leading zeros.

class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        num_list = list(num)
        res = self.getAllTerms(num_list)
        res2 = []
        for line in res:
            charact_line = ''.join(line)
            go_further = False
            search_number = True
            for j in range(len(line)):
                elem = line[j]
                if elem in ["+", "-", "*"]:
                    go_further = False
                    search_number = True
                else:
                    if (search_number) and (j != len(line) - 1):
                        if go_further:
                                break
                        if elem == "0":
                            go_further = True
                        else:
                            search_number = False
            if go_further:
                continue
            try:
                if eval(charact_line) == target:
                    res2.append(charact_line)
            except:
                continue
        return res2

    def getAllTerms(self, num_list):
        if len(num_list) == 1:
            return [num_list]
        res = self.getAllTerms(num_list[1:])
        final_res = []
        for line in res:
            temp = [num_list[0]]
            temp.append("+")
            temp.extend(line)
            final_res.append(temp)
            temp = [num_list[0]]
            temp.append("-")
            temp.extend(line)
            final_res.append(temp)
            temp = [num_list[0]]
            temp.append("*")
            temp.extend(line)
            final_res.append(temp)
            temp = [num_list[0]]
            temp.extend(line)
            final_res.append(temp)
        return final_res
