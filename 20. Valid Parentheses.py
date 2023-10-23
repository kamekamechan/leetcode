class Solution:
    def isValid(self, s: str) -> bool:
        lett_pair = {"(":")", "{":"}", "[":"]"}

        lett_stack = []

        for lett in s:
            if lett in lett_pair.keys():
                lett_stack.append(lett_pair[lett])
            elif(len(lett_stack) == 0 ):
                return False
            elif(lett_stack[-1] == lett):
                lett_stack.pop()
            else:
                return False
        
        if(len(lett_stack) == 0):
            return True
        
test = Solution()
print(test.isValid("(([]){})"))