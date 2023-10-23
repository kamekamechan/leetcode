import re

class Solution:
    def calculate(self, s: str) -> int:
        operators = ['+', '-', '(', ')']
        s = s.replace(' ', '')

        string_stack = []
        for index, char in enumerate(s):
            if char in operators:
                string_stack.append(char)
            else:
                if(string_stack == [] or type(string_stack[-1]) == str):
                    string_stack.append(int(char))
                else:
                    string_stack[-1] *= 10
                    string_stack[-1] += int(char)

        nums_out = 0

        plus_sign = 1
        before_plus_sign = []
        for index, var_str in enumerate(string_stack):
            if(index == 0):
                if(var_str in operators):
                    if(var_str == '('):
                        before_plus_sign.append(plus_sign)
                else:
                    nums_out += var_str

            else:
                if(var_str in operators):
                    if(var_str == '('):
                        if(string_stack[index-1] == '-'):
                            before_plus_sign.append(plus_sign)
                            plus_sign *= -1
                        else:
                            before_plus_sign.append(plus_sign)
                    elif(var_str == ')'):
                        plus_sign = before_plus_sign.pop()
                else:
                    if(string_stack[index-1] == '-'):
                        nums_out += plus_sign * var_str * -1
                    else:
                        nums_out += plus_sign * var_str

        return nums_out
            
test = Solution()
print(test.test("(3-(5-(8)-(2+(9-(0-(8-(2))))-(4))-(4)))"))