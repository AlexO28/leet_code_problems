class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        mapped_dict = {}
        for num in nums:
            mapped_num = self.mapNumber(num, mapping)
            if mapped_num in mapped_dict:
                mapped_dict[mapped_num].append(num)
            else:
                mapped_dict[mapped_num] = [num]
        keys = list(mapped_dict.keys())
        keys.sort()
        res = []
        for key in keys:
            res.extend(mapped_dict[key])
        return res
        
    def mapNumber(self, num, mapping):
        return int("".join([str(mapping[int(elem)]) for elem in list(str(num))]))
