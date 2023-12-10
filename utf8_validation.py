# Given an integer array data representing the data, return whether it is a valid UTF-8 encoding (i.e. it translates to a sequence of valid UTF-8 encoded characters).
class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        data_bytes = [bin(dat)[2:] for dat in data]
        data_bytes = []
        for j in range(len(data)):
            candidate = bin(data[j])[2:]
            if len(candidate) < 8:
                candidate = "0"*(8-len(candidate)) + candidate
            data_bytes.append(candidate)
        pos = 0
        while pos < len(data_bytes):
            check = False
            if self.validateOneByte(data_bytes[pos]):
                check = True
                pos += 1
            if (not check) & (pos + 1 < len(data_bytes)):
                if self.validateTwoBytes(data_bytes[pos], data_bytes[pos+1]):
                    check = True
                    pos += 2
            if (not check) & (pos + 2 < len(data_bytes)):
                if self.validateThreeBytes(data_bytes[pos], data_bytes[pos+1],\
                                           data_bytes[pos+2]):
                    check = True
                    pos += 3
            if (not check) & (pos + 3 < len(data_bytes)):
                if self.validateFourBytes(data_bytes[pos], data_bytes[pos+1],\
                                          data_bytes[pos+2], data_bytes[pos+3]):
                    check = True
                    pos += 4
            if not check:
                return False
        return True

    def validateOneByte(self, byte):
        return byte[0] == "0"

    def validateTwoBytes(self, byte1, byte2):
        return (byte1[:3] == "110") & (byte2[:2] == "10")

    def validateThreeBytes(self, byte1, byte2, byte3):
        return (byte1[:4] == "1110") & (byte2[:2] == "10") & (byte3[:2] == "10")

    def validateFourBytes(self, byte1, byte2, byte3, byte4):
        return (byte1[:5] == "11110") & (byte2[:2] == "10") &\
               (byte3[:2] == "10") & (byte4[:2] == "10")
