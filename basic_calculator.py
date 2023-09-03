class Solution:
    def calculateExpression(self, symbols, pos):
        new_symbols = []
        i = pos
        while True:
            if symbols[i] == "(":
                res, pos = self.calculateExpression(symbols, i+1)
                new_symbols.append(res)
                i = pos + 1
            elif symbols[i] == ")":
                return str(eval(''.join(new_symbols))), i
            else:
                new_symbols.append(symbols[i])
                i += 1  
            if i >= len(symbols):
                break

    def calculate(self, s: str) -> int:
        symbols = list(s)
        i = 0
        new_symbols = []
        while True:
            if symbols[i] == "(":
                res, pos = self.calculateExpression(symbols, i+1)
                new_symbols.append(res)
                i = pos + 1
            else:
                new_symbols.append(symbols[i])
                i += 1
            if i >= len(symbols):
                break
        return int(eval(''.join(new_symbols)))
