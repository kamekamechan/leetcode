class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        token_stack = []
        operator = ["+", "-", "*", "/"]

        for token in tokens:
            if(token in operator):
                num2 = int(token_stack.pop())
                num1 = int(token_stack.pop())
                if(token == "+"):
                    token_stack.append(num1 + num2)
                elif(token == "-"):
                    token_stack.append(num1 - num2)
                elif(token == "*"):
                    token_stack.append(num1 * num2)
                elif(token == "/"):
                    token_stack.append(int(num1 / num2))
            else:
                token_stack.append(token)
            
        return token_stack[0]

test = Solution()
print(test.evalRPN(["2","1","+","3","*"]))