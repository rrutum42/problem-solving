class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk =[]
        for token in tokens:
            if token == "+" or token == "-" or token == "/" or token == "*":
                second = stk.pop()
                first = stk.pop()
                if token == "+":
                    val = first + second
                elif token == "-":
                    val = first - second
                elif token == "/":
                    val = int(first / second)
                elif token == "*":
                    val = first * second
                stk.append(val)
            else:
                stk.append(int(token))
            
        return stk.pop()
        