# class MinStack:

#     def __init__(self):
#         self.min_value_array = []
#         self.num_stack = []

#     def push(self, val: int) -> None:
#         self.num_stack.append(val)
#         if(self.min_value_array == []):
#             self.min_value_array.append(val)
#         elif(self.min_value_array[-1] > val):
#             self.min_value_array.append(val)

#     def pop(self) -> None:
#         if(self.num_stack != []):
#             if(self.min_value_array[-1] == self.num_stack[-1]):
#                 self.min_value_array.pop()
#             self.num_stack.pop()

#     def top(self) -> int:
#         if(self.num_stack != []):
#             return self.num_stack[-1]

#     def getMin(self) -> int:
#         if(self.min_value_array != []):
#             return self.min_value_array[-1]


class MinStack:

    def __init__(self):
        self.sort_array = []
        self.num_stack = []

    def push(self, val: int) -> None:
        self.num_stack.append(val)
        self.sort_array.append(val)
        self.sort_array.sort(reverse=True)

    def pop(self) -> None:
        if(self.num_stack != []):
            pop_num = self.num_stack.pop()
            self.sort_array.pop(self.sort_array.index(pop_num))

    def top(self) -> int:
        if(self.num_stack != []):
            return self.num_stack[-1]

    def getMin(self) -> int:
        if(self.sort_array != []):
            return self.sort_array[-1]
        
test = MinStack()
print(test.push(0))
print(test.push(1))
print(test.push(0))
print(test.getMin())
print(test.pop())
print(test.getMin())


print("test case 1")
test = MinStack()
print(test.push(-2))
print(test.push(0))
print(test.push(-3))
print(test.getMin())
print(test.pop())
print(test.top())
print(test.getMin())

