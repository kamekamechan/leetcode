class Solution:
    def mySqrt(self, x: int) -> int:
        if(x == 0):
            return 0

        ans_num = 1
        while(ans_num * ans_num <= x):
            ans_num *= 2
        
        for i in range(ans_num//2, ans_num):
            if(i * i > x):
                return i-1
            elif(i == ans_num -1):
                return i

test = Solution()
print(test.mySqrt(x = 4))