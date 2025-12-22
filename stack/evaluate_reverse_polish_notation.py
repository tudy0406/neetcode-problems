class Solution:
    def sumP(self, val1: int, val2: int) -> int:
        return val1 + val2
    
    def subP(self, val1: int, val2: int) -> int:
        return val1-val2    

    def mulP(self, val1: int, val2: int) -> int:
        return val1*val2

    def divP(self, val1: int, val2: int) -> int:
        return int(val1/val2)

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c not in {'+', '-', '*', '/'}:
                stack.append(int(c))
            else:
                if len(stack) >= 2:
                    val2 = stack.pop()
                    val1 = stack.pop()
                match c:
                    case '+':
                        stack.append(self.sumP(val1, val2))
                    case '-':
                        stack.append(self.subP(val1, val2))
                    case '*':
                        stack.append(self.mulP(val1, val2))
                    case '/':
                        stack.append(self.divP(val1, val2))
        return stack.pop()