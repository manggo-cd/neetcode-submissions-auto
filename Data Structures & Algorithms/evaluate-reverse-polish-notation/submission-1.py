class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        while len(tokens) > 1:
            for i in range(len(tokens)):
                if tokens[i] in "+-*/":
                    a = int(tokens[i-2])
                    b = int(tokens[i-1])

                    if tokens[i] == "+":
                        res = a + b
                    if tokens[i] == "-":
                        res = a - b
                    if tokens[i] == "*":
                        res = a * b
                    if tokens[i] == "/":
                        res = int(a / b)

                    tokens = tokens[:i-2] + [str(res)] + tokens[i+1:]
                    break
        return int(tokens[0])

        