class Solution:
    def myPow(self, x: float, n: int) -> float:
        count = 1
        output = x
        if(abs(n)>0):
            while(2*count <= abs(n)):
                output *= output
                count += count
            
            for i in range(abs(n)-count):
                output *= x
            
            if(n>0):
                return output
            elif(n<0):
                return 1/output

        elif(n==0):
            return 1
        

test = Solution()
print(test.myPow(x = 2.00000, n = 10))