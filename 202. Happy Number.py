class Solution:
    def isHappy(self, n: int) -> bool:
        happy_dic = {}
        current_num = n
        while(current_num != 1):
            current_num = self.happy_calc(current_num)
            if(current_num in happy_dic.keys()):
                return False
            else:
                happy_dic[current_num] = 1
        return True

    def happy_calc(self, n:int):
        output = 0
        current_num = n
        while(current_num != 0):
            output += (current_num % 10) ** 2
            current_num = current_num // 10
        return output
    
test  = Solution()
print(test.isHappy(2))